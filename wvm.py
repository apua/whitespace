# -*- coding=utf8 -*-

'''
usage:
    $ py3 wvm.py $FILE [ $LEXICAL_TOKEN ]

doctest::
>>> # output 1~10
>>> code = "SSSTLLSSSTSS SSTTLSLSTLSTSSSTSTSLTLSSSSSTLTSSSSLSSSSTSTTLTSSTLTSSTSS STSTLLSLSTS SSSTTLLSSSTS SSTSTLSLLLLL"
>>> # factorial
>>> code = "SSSSLSSSTSSSTSTLTTSSSSTLSSSTTSTTTSLTTSSSSTSLSSSTTTSTSSLTTSSSSTTLSSSTTSSTSTLTTSSSSTSSLSSSTTTSSTSLTTSSSSTSTLSSSTSSSSSLTTSSSSTTSLSSSTTSSSSTLTTSSSSTTTLSSSTSSSSSLTTSSSSTSSSLSSSTTSTTTSLTTSSSSTSSTLSSSTTTSTSTLTTSSSSTSTSLSSSTTSTTSTLTTSSSSTSTTLSSSTTSSSTSLTTSSSSTTSSLSSSTTSSTSTLTTSSSSTTSTLSSSTTTSSTSLTTSSSSTTTSLSSSTTTSTSLTTSSSSTTTTLSSSTSSSSSLTTSSSSTSSSSLSSSSLTTSSSSTSTSSLSSSTSSSSTLTTSSSSTSTSTLSSSTSSSSSLTTSSSSTSTTSLSSSTTTTSTLTTSSSSTSTTTLSSSTSSSSSLTTSSSSTTSSSLSSSSLTTSSSSSLLSTSTTTSTTTSTTTSSTSSTTSTSSTSTTTSTSSSTTSSTSTLSSSTTSSTSSLTLTTSSSTTSSTSSLTTTLSTSTTSSTTSSTTSSSSTSTTSSSTTSTTTSTSSLSSSTTSSTSSLTTTTLSTSSSTSTSSLLSTSTTTSTTTSTTTSSTSSTTSTSSTSTTTSTSSSTTSSTSTLTLSTLSTSTTSTTTSSTTSSTSTSTTTSTTTSTTSTTSSSTTSTSSTSTTSTTTSSTTSSTSTLLLLLSSSTTSSTTSSTTSSSSTSTTSSSTTSTTTSTSSLSLSSSSTLTSSTLTSSTTSSTTSSTTSSSSTSTTSSSTTSTTTSTSSSTTSSSTSSTTSSSSTSTTTSSTTSTTSSTSTLSLSSSSTLTSSTLSTSTTSSTTSSTTSSSSTSTTSSSTTSTTTSTSSLTSSLLTLLSSSTTSSTTSSTTSSSSTSTTSSSTTSTTTSTSSSTTSSSTSSTTSSSSTSTTTSSTTSTTSSTSTLSSSTLSLLLTLLSSSTTSSSSTSTTSSTSSSTTSSTSSLTSSSLTLLSSSTTTSTTTSTTTSSTSSTTSTSSTSTTTSTSSSTTSSTSTLSLSTTTSLSLTSSTTTSTTTSTTTSSTSSTTSTSSTSTTTSTSSSTTSSTSTSTSTTTTTSTTSSTSTSTTSTTTSSTTSSTSSLTLSSSSSTLTSSSLSLSTTTSTTTSTTTSSTSSTTSTSSTSTTTSTSSSTTSSTSTLLSSSTTTSTTTSTTTSSTSSTTSTSSTSTTTSTSSSTTSSTSTSTSTTTTTSTTSSTSTSTTSTTTSSTTSSTSSLSLLSLLLTLLSSSTTTSSTSSTTSSTSTSTTSSSSTSTTSSTSSLSLSSLSTLTSTTTSLSSSSTSTSLTSSTLTSSTTTSSTSSTTSSTSTSTTSSSSTSTTSSTSSSTSTTTTTSTTSSTSTSTTSTTTSSTTSSTSSLSLLSSSTLTSSSLSLSTTTSSTSSTTSSTSTSTTSSSSTSTTSSTSSLLSSSTTTSSTSSTTSSTSTSTTSSSSTSTTSSTSSSTSTTTTTSTTSSTSTSTTSTTTSSTTSSTSSLSLLSSSTLTSSSSSSSLTTSLTLLSSSTTSTTTSSTTSSTSTSTTTSTTTSTTSTTSSSTTSTSSTSTTSTTTSSTTSSTSTLSSSTSTSLSSSTTSTLTLSSTLSSLTLL"
>>> 
>>> run_wvm(code)
'''

def run_wvm(whitespace_code, lexical_token='STL'):
    '''compile Whitespace code and run VM'''

    def compile_to_IR(
        source, token,
        clean = lambda source,token: ''.join(filter(token.__contains__,source)).translate(str.maketrans(token,'STL')) ,
        to_num = lambda s: eval('+-'[s[0]!='S']+'0b'+s[1:].translate({83:48,84:49})) ,
        T = ((r'LSS([ST]+)L',     None                                          ),
             (r'LST([ST]+)L',     'CPSR.append(c+1) or {}'                      ),
             (r'LSL([ST]+)L',     '{}'                                          ),
             (r'LTS([ST]+)L',     '{} if Stack.pop()==0 else c+1'               ),
             (r'LTT([ST]+)L',     '{} if Stack.pop()<0 else c+1'                ),
             (r'SS([ST][ST]+)L',  'Stack.append({})'                            ),
             (r'STS([ST][ST]+)L', 'Stack.append(Stack[-{}])'                    ),
             (r'STL([ST][ST]+)L', 'any(Stack.pop(-2) and 0 for t in range({}))' ),
             (r'SLS()',           'Stack.append(Stack[-1])'                     ),
             (r'SLT()',           'Stack.insert(-1,Stack.pop())'                ),
             (r'SLL()',           'Stack.pop() and 0'                           ),
             (r'TSSS()',          'Stack.append(Stack.pop(-2)+Stack.pop())'     ),
             (r'TSST()',          'Stack.append(Stack.pop(-2)-Stack.pop())'     ),
             (r'TSSL()',          'Stack.append(Stack.pop(-2)*Stack.pop())'     ),
             (r'TSTS()',          'Stack.append(Stack.pop(-2)//Stack.pop())'    ),
             (r'TSTT()',          'Stack.append(Stack.pop(-2)%Stack.pop())'     ),
             (r'TTS()',           'Heap.__setitem__(Stack.pop(-2), Stack.pop())'),
             (r'TTT()',           'Stack.append(Heap.__getitem__(Stack.pop()))' ),
             (r'TLSS()',          'putchar(chr(Stack.pop()))'                   ),
             (r'TLST()',          'putchar(str(Stack.pop()))'                   ),
             (r'TLTS()',          'Heap.__setitem__(Stack.pop(),ord(getchar()))'),
             (r'TLTT()',          'Heap.__setitem__(Stack.pop(),int(input()))'  ),
             (r'LTL()',           'CPSR.pop()'                                  ),
             (r'LLL()',           '-1'                                          ))
        ):
        '''
        clean: translate source code to [STL]+
        to_num: translate [ST][ST]+ to number
        T: intermediate language translation mapping table
           columns: [pattern, translate map]
        '''

        # 清程式碼
        W = clean(source,token)

        # 建 IR 和 label mapping
        import re
        IR = intermediate_representation = []
        R = pattern = '|'.join(t[0] for t in T)
        L = temporary_label_mapping = {}
        for match in re.finditer(R,W,re.VERBOSE):
            for k, v in enumerate(match.groups()):
                if v is not None:
                    if k==0:
                        L[v] = len(IR)
                    else:
                        IR.append((T[k][1], to_num(v) if v and k>=5 else v))
                    break

        # 根據 label mapping 再修正 (於是 label mapping 就不需要了)
        IR = [(ir[0],L[ir[1]]) if ir[1] in L else ir for ir in IR]

        return IR


    def interprete_IR(IR, Components={'Stack':[],'Heap':{},'LR':[],'PC':[0]}):
        '''
        Components:
            Stack: accumulator
            Heap: memory
            LR: link register which is also a stack
            PC: program counter with length 1
        '''

        def putchar(c):
            '''output a given charactor'''
            from sys import stdout as o
            o.write(c)
            o.flush()

        def getchar():
            '''get a charactor from stdin'''
            from sys import stdin as i
            return i.read(1)


    IR = compile_to_IR(whitespace_code, lexical_token)

    # output test
    from pprint import pprint as p
    p(list(enumerate(IR)))


if __name__=='__main__':
    import sys
    run_wvm(whitespace_code=open(sys.argv[1]).read(),
            lexical_token=' \t\n' if len(sys.argv)<3 else sys.argv[2])
