def CCCCCCC(num,CODE= '''
SSSSLTLTTSSSSLSSSSLTTTTSSTSLSLTSSLSSSTLSLSSLSSSSSLSLSTTSTTSTSSTLSSTLSSSTLSLSTTTSLSSLSSSSSLTTTTSSSSSSTLSLTTTSSSSSLSLTTTSTSSSTSSSSLSLTTTLSSSTLTTTTSSSLSSSLTLSTLLL
'''):

    K = '''(lambda _,A=[],B=[str(num)],C=[],H={},I=[],L={},O='S.append({});S.append(S[-{}]);any(S.pop(-2) and 0 for t in range({}));S.append(S[-1]);S.insert(-1,S.pop());S.pop() and 0;S.append(S.pop(-2)+S.pop());S.append(S.pop(-2)-S.pop());S.append(S.pop(-2)*S.pop());S.append(S.pop(-2)//S.pop());S.append(S.pop(-2)%S.pop());H.__setitem__(S.pop(-2), S.pop());S.append(H.__getitem__(S.pop()));A.append(chr(S.pop()));A.append(str(S.pop()));H.__setitem__(S.pop(),ord(getchar()));H.__setitem__(S.pop(),int(B.pop(0)));0;C.append(c+1) or {};{};{} if S.pop()==0 else c+1;{} if S.pop()<0 else c+1;C.pop();-1'.split(';'),P=[0],S=[]:[[I.append((p,v))if p!=17 else L.__setitem__(v,len(I))for p,v in enumerate(m.groups())if v]for m in __import__('re').finditer('(?:S(?:S([ST]{2,})L|TS([ST]{2,})L|TL([ST]{2,})L|(LS)|(LT)|(LL))|TS(?:(SS)|(ST)|(SL)|(TS)|(TT))|TT(?:(S)|(T))|TL(?:(SS)|(ST)|(TS)|(TT))|L(?:SS([ST]+)L|ST([ST]+)L|SL([ST]+)L|TS([ST]+)L|TT([ST]+)L|(TL)|(LL)))',''.join(c for c in _ if c in'STL'),64)]and[c>-1and P.append([S,H,A,B]and eval(O[I[c][0]].format(L.get(I[c][1])if I[c][0]>2 else eval('+-'[I[c][1][0]!='S']+'0b'+I[c][1][1:].translate({83:48,84:49})))+(I[c][0]<17and' or c+1'or'')))for c in P]and''.join(A))(CODE)'''
    
    return eval(K)


if __name__=='__main__':
  n = 25; print(n, CCCCCCC(n))
  n = 13; print(n, CCCCCCC(n))
  n = 10; print(n, CCCCCCC(n))
  n = 16; print(n, CCCCCCC(n))
