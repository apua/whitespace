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
        T = ((r'SS([ST][ST]+)L',  'stack.append({}) or PC.append(PC.pop()+1)'                                ),
             (r'STS([ST][ST]+)L', 'stack.append(stack[-{}]) or PC.append(PC.pop()+1)'                        ),
             (r'STL([ST][ST]+)L', 'stack.__delslice__(len(stack)-1+{},len(stack)-1) or PC.append(PC.pop()+1)'),
             (r'SLS()',           'stack.append(stack[-1]) or PC.append(PC.pop()+1)'                         ),
             (r'SLT()',           'stack.insert(-1,stack.pop()) or PC.append(PC.pop()+1)'                    ),
             (r'SLL()',           'stack.pop() and False or PC.append(PC.pop()+1)'                           ),
             (r'TSSS()',          'stack.append(stack.pop(-2)+stack.pop()) or PC.append(PC.pop()+1)'         ),
             (r'TSST()',          'stack.append(stack.pop(-2)-stack.pop()) or PC.append(PC.pop()+1)'         ),
             (r'TSSL()',          'stack.append(stack.pop(-2)*stack.pop()) or PC.append(PC.pop()+1)'         ),
             (r'TSTS()',          'stack.append(stack.pop(-2)//stack.pop()) or PC.append(PC.pop()+1)'        ),
             (r'TSTT()',          'stack.append(stack.pop(-2)%stack.pop()) or PC.append(PC.pop()+1)'         ),
             (r'TTS()',           'heap.__setitem__(stack.pop(-2), stack.pop()) or PC.append(PC.pop()+1)'    ),
             (r'TTT()',           'stack.append(heap.__getitem__(stack.pop())) or PC.append(PC.pop()+1)'     ),
             (r'TLSS()',          'putchar(chr(stack.pop())) or PC.append(PC.pop()+1)'                       ),
             (r'TLST()',          'putchar(str(stack.pop())) or PC.append(PC.pop()+1)'                       ),
             (r'TLTS()',          'heap.__setitem__(stack.pop(),ord(getchar())) or PC.append(PC.pop()+1)'    ),
             (r'TLTT()',          'heap.__setitem__(stack.pop(),int(input())) or PC.append(PC.pop()+1)'      ),
             (r'LSS([ST]+)L',     None                                                                       ),
             (r'LST([ST]+)L',     'PC.append(LR.append(PC.pop()+1) or {})'                                   ),
             (r'LSL([ST]+)L',     'PC.__setitem__(0, {})'                                                    ),
             (r'LTS([ST]+)L',     'PC.__setitem__(0, {} if stack.pop()==0 else PC[0]+1)'                     ),
             (r'LTT([ST]+)L',     'PC.__setitem__(0, {} if stack.pop()<0 else PC[0]+1)'                      ),
             (r'LTL()',           'PC.__setitem__(0, LR.pop())'                                              ),
             (r'LLL()',           'PC.__setitem__(0, None)'                                                  ))
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
                    if k==17:
                        L[v] = len(IR)
                    else:
                        IR.append((k,v))
                    break

        # 換算 label 和 number
        # value: (trans to num) if k<3 else (get from label)
        IR = [ T[k][1].format(to_num(v) if k<3 else L.get(v)) for k,v in IR ]

        return IR


    def interprete_IR(text, stack=[], heap={}, LR=[], PC=[0]):
        '''
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

        while PC[0] is not None:
            instruction = text[PC[0]]
            eval(instruction) # do something, then PC+=1 or jump

            #tmp=input( 'PC/LR: {},{} stack: {}, heap: {}'.format(PC,LR,stack,heap) )


    IR = compile_to_IR(whitespace_code, lexical_token)

    # output test
    #from pprint import pprint as p
    #p(list(enumerate(IR)))

    interprete_IR(IR)


if __name__=='__main__':
    import sys
    run_wvm(whitespace_code=open(sys.argv[1]).read(),
            lexical_token=' \t\n' if len(sys.argv)<3 else sys.argv[2])
