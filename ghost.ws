let ``ghost := year -> opacity``,
SSSSL
what we want is the inverse of ghost, write ``f := opactity -> year``
TLTTSSSSLTTT
get number N and put into stack
SSSTSSTTTSSSTSSSSLTSST
let N := opacity - 10000
SLSLTSSL
if N = 0, then the ghost is newborn
SSSTLSLSSLSSSSSLSLSTTSTTSTSST
otherwise, let F := [0,1,1,2,3,5,..] is a Fibnacci seq w/ index [0,1,2,3,4,...],
LSS TL
we find that N + (F[1]+1) + (F[2]+1) +...+ (F[k]+1) = 1 if F[k+1] = f(N) 
SSSTL SLS TTT SLS SLS
for example, if N = -25 and F[k+1] = f(N) = 13 (i.e, F[k] = 8),
SSSSL TTT TSSS
N + (F[1]+1) + (F[2]+1) +...+ (F[f(N)]) = -25 + (1+1) + (1+1) +..+ (8+1)
SSSTL SLT TTS
= -25 + 2 + 2 + 3 + 4 + 6 + 9 = 1 
SSSSL SLT TTS
by this theorem, we can easily get f(N) as generating Fibnacci seq if f(N) in F
TSSS TSSS
on the other hand, if f(N) is not in F, it means, 
SLS LTT TL
there is f(M) in F such that f(N)-f(M) = N-M
SSSTL TTT TSSS
for example, len N := -22, M := -25
LSS SL
f(N)-f(M) = 16-13 = 3 = (-22)-(-25) = N-M
TLST
so, we can use the simple idea, implement function f with a while loop
LLL
:)
