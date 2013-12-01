ZZZZZZZZLet ``ghost := year -> opacity``, what we want is the inverse of ghost, 
ZZZZZZZZSSSSWTWTTSSSSWTTT
ZZZZZZZZwrite ``f := opactity -> year``
ZZZZZZZZSSSTSSTTTSSSTSSSSWTSST
ZZZZZZZZLet N := opacity - 10000 . If N = 0, then the ghost is newborn; otherwise,
ZZZZZZZZSWSWTSSW
ZZZZZZZZLet F := [0,1,1,2,3,5,..] is a Fibnacci seq w/ index [0,1,2,3,4,...],
ZZZZZZZZSSSTWSWSSWSSSSSWSWSTTSTTSTSST
ZZZZZZZZwe find that
ZZZZZZZZWSS TW
ZZZZZZZZSSN + (F[1]+1) + (F[2]+1) +...+ (F[k]+1) = 1 if F[k+1] = f(N) .
ZZZZZZZZSTW SWS TTT SWS SWS
ZZZZZZZZFor example, if N = -25 and F[k+1] = f(N) = 13 (i.e, F[k] = 8),
ZZZZZZZZSSSSW TTT TSSS
ZZZZZZZZSSN + (F[1]+1) + (F[2]+1) +...+ (F[f(N)]) = -25 + (1+1) + (1+1) +..+ (8+1)
ZZZZZZZZSTW SWT TTS
ZZZZZZZZ= -25 + 2 + 2 + 3 + 4 + 6 + 9 = 1 
ZZZZZZZZSSSSW SWT TTS
ZZZZZZZZBy this theorem, we can easily get f(N) as generating Fibnacci seq if f(N) in F
ZZZZZZZZTSSS TSSS
ZZZZZZZZOn the other hand, if f(N) is not in F, it means, there is f(M) in F such that
ZZZZZZZZSWS WTT TW
ZZZZZZZZSSf(N)-f(M) = N-M
ZZZZZZZZSTW TTT TSSS
ZZZZZZZZFor example, let N := -22 and M := -25, then 
ZZZZZZZZWSS SW
ZZZZZZZZTWf(N)-f(M) = 16-13 = 3 = (-22)-(-25) = N-M
ZZZZZZZZST
ZZZZZZZZso, we can use the simple idea, implement function f with a while loop
ZZZZZZZZWWW
ZZZZZZZZ:)
