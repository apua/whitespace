Let ``ghost := year -> opacity``, what we want is the inverse of ghost, 
SSSSLTLTTSSSSLTTT
write ``f := opactity -> year``
SSSTSSTTTSSSTSSSSLTSST
Let N := opacity - 10000 . If N = 0, then the ghost is newborn; otherwise,
SLSLTSSL
let F := [0,1,1,2,3,5,..] is a Fibnacci seq w/ index [0,1,2,3,4,...],
SSSTLSLSSLSSSSSLSLSTTSTTSTSST
we find that
LSS TL
  N + (F[1]+1) + (F[2]+1) +...+ (F[k]+1) = 1 if F[k+1] = f(N) .
SSSTL SLS TTT SLS SLS
For example, if N = -25 and F[k+1] = f(N) = 13 (i.e, F[k] = 8),
SSSSL TTT TSSS
  N + (F[1]+1) + (F[2]+1) +...+ (F[f(N)]) = -25 + (1+1) + (1+1) +..+ (8+1)
SSSTL SLT TTS
= -25 + 2 + 2 + 3 + 4 + 6 + 9 = 1 
SSSSL SLT TTS
By this theorem, we can easily get f(N) as generating Fibnacci seq if f(N) in F
TSSS TSSS
On the other hand, if f(N) is not in F, it means, there is f(M) in F such that
SLS LTT TL
  f(N)-f(M) = N-M
SSSTL TTT TSSS
For example, let N := -22 and M := -25, then 
LSS SL
  f(N)-f(M) = 16-13 = 3 = (-22)-(-25) = N-M
TLST
so, we can use the simple idea, implement function f with a while loop
LLL
:)
