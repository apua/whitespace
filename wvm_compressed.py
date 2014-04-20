def run_wvm(whitespace_code, lexical_token='STL'):
    '''compile Whitespace code and run VM'''

    def compile_to_IR(
        source, token, IR = [], L = {},
        R = 'SS([ST][ST]+)L|STS([ST][ST]+)L|STL([ST][ST]+)L|SLS()|SLT()|SLL()|TSSS()|TSST()|TSSL()|TSTS()|TSTT()|TTS()|TTT()|TLSS()|TLST()|TLTS()|TLTT()|LSS([ST]+)L|LST([ST]+)L|LSL([ST]+)L|LTS([ST]+)L|LTT([ST]+)L|LTL()|LLL()',
        T = ('S.append({})','S.append(S[-{}])','S.__delslice__(len(S)-1+{},len(S)-1)','S.append(S[-1])','S.insert(-1,S.pop())','S.pop()*0',
             'S.append(S.pop(-2)+S.pop())','S.append(S.pop(-2)-S.pop())','S.append(S.pop(-2)*S.pop())','S.append(S.pop(-2)//S.pop())','S.append(S.pop(-2)%S.pop())',
             'H.__setitem__(S.pop(-2), S.pop())','S.append(H.__getitem__(S.pop()))',
             'putchar(chr(S.pop()))','putchar(str(S.pop()))','H.__setitem__(S.pop(),ord(getchar()))','H.__setitem__(S.pop(),int(input()))',
             None,'^(0,LR.append(PC[0]+1) or {})','^(0,{})','^(0,{} if S.pop()==0 else PC[0]+1)','^(0,{} if S.pop()<0 else PC[0]+1)','^(0,LR.pop())','^(0,-1)')
        ):
        for match in __import__('re').finditer(R,''.join(filter(token.__contains__,source)).translate(str.maketrans(token,'STL'))):
            for k, v in enumerate(match.groups()):
                if v is not None:
                    if k==17:
                        L[v] = len(IR)
                    else:
                        IR.append((k,v))
                    break
        return [ 'lambda S,H,LR,PC,putchar=lambda c,o=__import__("sys").stdout: o.write(c) and o.flush(), getchar=lambda i=__import__("sys").stdin: i.read(1):'+\
                 T[k].format(eval('+-'[v[0]!='S']+'0b'+v[1:].translate({83:48,84:49})) if k<3 else L.get(v)).replace('^','PC.__setitem__')+(' or PC.append(PC.pop()+1)' if k<17 else '') for k,v in IR ]             


    def interprete_IR(text, component=([],{},[],[0])):
        any(1 if component[3][0]<0 else eval(text[component[3][0]])(*component) for i in __import__('itertools').cycle([0]))


    interprete_IR(compile_to_IR(whitespace_code, lexical_token))


if __name__=='__main__':
    import sys
    run_wvm(whitespace_code=open(sys.argv[1]).read(), lexical_token=' \t\n' if len(sys.argv)<3 else sys.argv[2])
