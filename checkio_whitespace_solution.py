def checkio(n,wvm=lambda s,t='\u2000\u2001\u2002',I=[],L={}:any(next(L.update({v:len(I)})if k==17 else I.append((k,v))for k,v in enumerate(match.groups())if v!=None)for match in __import__('re').finditer('SS([ST][ST]+)L|STS([ST][ST]+)L|STL([ST][ST]+)L|SLS()|SLT()|SLL()|TSSS()|TSST()|TSSL()|TSTS()|TSTT()|TTS()|TTT()|TLSS()|TLST()|TLTS()|TLTT()|LSS([ST]+)L|LST([ST]+)L|LSL([ST]+)L|LTS([ST]+)L|LTT([ST]+)L|LTL()|LLL()',''.join(filter(t.__contains__,s)).translate(str.maketrans(t,'STL'))))or(lambda T,C=([],{},[],[0]):any(1if C[3][0]<0 else eval(T[C[3][0]])(*C)for i in __import__('itertools').cycle([0])))(['lambda S,H,R,P,putchar=lambda c,o=__import__("sys").stdout:o.write(c)and o.flush(),getchar=lambda i=__import__("sys").stdin:i.read(1):'+('S.A({})','S.A(S[-{}])','S.__delslice__(len(S)-1+{},len(S)-1)','S.A(S[-1])','S.insert(-1,S.B())','S.B()*0','S.A(S.B(-2)+S.B())','S.A(S.B(-2)-S.B())','S.A(S.B(-2)*S.B())','S.A(S.B(-2)//S.B())','S.A(S.B(-2)%S.B())','H.__setitem__(S.B(-2),S.B())','S.A(H.__getitem__(S.B()))','putchar(chr(S.B()))','putchar(str(S.B()))','H.__setitem__(S.B(),ord(getchar()))','H.__setitem__(S.B(),int(input()))',0,'^(0,R.A(P[0]+1) or {})','^(0,{})','^(0,{}if S.B()==0 else P[0]+1)','^(0,{}if S.B()<0 else P[0]+1)','^(0,R.B())','^(0,-1)')[k].format(eval('+-'[v[0]!='S']+'0b'+v[1:].translate({83:48,84:49}))if k<3 else L.get(v)).replace('^','P.__setitem__').replace('A','append').replace('B','pop')+(' or P.append(P.pop()+1)'if k<17 else '')for k,v in I])):
     
    whitespace = '''
     
　　　　　　　　Let ``ghost := year -> opacity``, what we want is the inverse of ghost, 
　　　　　　　　                 
　　　　　　　　write ``f := opactity -> year``
　　　　　　　　                      
　　　　　　　　Let N := opacity - 10000 . If N = 0, then the ghost is newborn; otherwise,
　　　　　　　　        
　　　　　　　　Let F := [0,1,1,2,3,5,..] is a Fibnacci seq w/ index [0,1,2,3,4,...],
　　　　　　　　                             
　　　　　　　　we find that
　　　　　　　　      
　　　　　　　　  N + (F[1]+1) + (F[2]+1) +...+ (F[k]+1) = 1 if F[k+1] = f(N) .
　　　　　　　　                   
　　　　　　　　For example, if N = -25 and F[k+1] = f(N) = 13 (i.e, F[k] = 8),
　　　　　　　　              
　　　　　　　　  N + (F[1]+1) + (F[2]+1) +...+ (F[f(N)]) = -25 + (1+1) + (1+1) +..+ (8+1)
　　　　　　　　           
　　　　　　　　= -25 + 2 + 2 + 3 + 4 + 6 + 9 = 1 
　　　　　　　　             
　　　　　　　　By this theorem, we can easily get f(N) as generating Fibnacci seq if f(N) in F
　　　　　　　　         
　　　　　　　　On the other hand, if f(N) is not in F, it means, there is f(M) in F such that
　　　　　　　　          
　　　　　　　　  f(N)-f(M) = N-M
　　　　　　　　            
　　　　　　　　For example, let N := -22 and M := -25, then 
　　　　　　　　      
　　　　　　　　  f(N)-f(M) = 16-13 = 3 = (-22)-(-25) = N-M
　　　　　　　　  
　　　　　　　　so, we can use the simple idea, implement function f with a while loop
　　　　　　　　   
　　　　　　　　:)
 
    '''
     
    return wvm(whitespace)
