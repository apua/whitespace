def checkio(n, interpret_whitespace="(lambda _,A=[],B=[str(n)],C=[],H={},I=[],L={},O='S.append({});S.append(S[-{}]);any(S.pop(-2)and 0for t in range({}));S.append(S[-1]);S.insert(-1,S.pop());S.pop()and 0;S.append(S.pop(-2)+S.pop());S.append(S.pop(-2)-S.pop());S.append(S.pop(-2)*S.pop());S.append(S.pop(-2)//S.pop());S.append(S.pop(-2)%S.pop());H.__setitem__(S.pop(-2),S.pop());S.append(H.__getitem__(S.pop()));A.append(chr(S.pop()));A.append(str(S.pop()));H.__setitem__(S.pop(),ord(getchar()));H.__setitem__(S.pop(),int(B.pop(0)));0;C.append(c+1)or{};{};{}if S.pop()==0 else c+1;{}if S.pop()<0 else c+1;C.pop();-1'.split(';'),P=[0],S=[]:[[I.append((p,v))if p!=17 else L.__setitem__(v,len(I))for p,v in enumerate(m.groups())if v]for m in __import__('re').finditer('(?:S(?:S([ST]{2,})L|TS([ST]{2,})L|TL([ST]{2,})L|(LS)|(LT)|(LL))|TS(?:(SS)|(ST)|(SL)|(TS)|(TT))|TT(?:(S)|(T))|TL(?:(SS)|(ST)|(TS)|(TT))|L(?:SS([ST]+)L|ST([ST]+)L|SL([ST]+)L|TS([ST]+)L|TT([ST]+)L|(TL)|(LL)))',''.join(c for c in _ if c in'STL'),64)]and[c>-1and P.append([S,H,A,B]and eval(O[I[c][0]].format(L.get(I[c][1])if I[c][0]>2 else eval('+-'[I[c][1][0]!='S']+'0b'+I[c][1][1:].translate({83:48,84:49})))+(I[c][0]<17and' or c+1'or'')))for c in P]and int(''.join(A)))(''.join(c for c in whitespace if c in '\u2000\u2001\u2002').translate(str.maketrans('\u2000\u2001\u2002','STL')))"):
     
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
     
    return eval(interpret_whitespace)

