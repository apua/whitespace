def CCCCCCC(num,CODE= '''
# initial
SSSSL TLTT # {0: f(n)}
SSSSL # add 0
SSSSL TTT # [0,f(n)]
TSST # [K]

# if K==0: return
SLS
LTS SL

# initial fib
SSSTL SLS SLS SSSSL SLS # [K,1,1,1,0,0]
TTS TTS TSST # [K-1] {0:0, 1:1}

'LSS TL' #### loop ####
# [K]
SSSTL SLS TTT SLS SLS # [K,1,b,b,b]
SSSSL TTT TSSS # [K,1,b,b,a+b]
SSSTL SLT TTS # [K,1,b,b] {1:a+b}
SSSSL SLT TTS # [K,1,b] {0:b, 1:a+b}
TSSS TSSS # [K+b+1]

SLS LTT TL # if K<0: loop
SSSTL TTT TSSS # [K+a+b]

# n:0   1   2   3   4   5   6   7   8   9   10
# K:0   1   3   6   5   10  9   8   16  15  14
# b:        1   2       3           5

'LSS SL' ##### end #####
TLST # n
LLL
'''):

  
    global Stack, Heap, result, buff

    buff = [str(num)]
    result = []
    Stack = []
    Heap = {}
    L = {}
    I = []
    PCs = [0]
    CPSR = []
    
    Operations = [
      # stack manipulation
      'Stack.append({})',
      'Stack.append(Stack[-{}])',
      'any(Stack.pop(-2) and 0 for t in range({}))',
      'Stack.append(Stack[-1])',
      'Stack.insert(-1,Stack.pop())',
      'Stack.pop() and 0',
      # arithmetic
      'Stack.append(Stack.pop(-2)+Stack.pop())',
      'Stack.append(Stack.pop(-2)-Stack.pop())',
      'Stack.append(Stack.pop(-2)*Stack.pop())',
      'Stack.append(Stack.pop(-2)//Stack.pop())',
      'Stack.append(Stack.pop(-2)%Stack.pop())',
      # heap
      'Heap.__setitem__(Stack.pop(-2), Stack.pop())',
      'Stack.append(Heap.__getitem__(Stack.pop()))',
      # IO
      'result.append(chr(Stack.pop()))',
      'result.append(str(Stack.pop()))',
      'Heap.__setitem__(Stack.pop(),ord(getchar()))',
      'Heap.__setitem__(Stack.pop(),int(buff.pop(0)))',
      # flow
      0,
      'CPSR.append(c+1) or {}',
      '{}',
      '{} if Stack.pop()==0 else c+1',
      '{} if Stack.pop()<0 else c+1',
      'CPSR.pop()',
      '-1',
    ]
    
    any(
      any( I.append((p,v)) if p!=17 else L.__setitem__(v, len(I))
        for p,v in enumerate(m.groups()) if v )
      for m in __import__('re').finditer('(?:S(?:S([ST]{2,})L|TS([ST]{2,})L|TL([ST]{2,})L|(LS)|(LT)|(LL))|TS(?:(SS)|(ST)|(SL)|(TS)|(TT))|TT(?:(S)|(T))|TL(?:(SS)|(ST)|(TS)|(TT))|L(?:SS([ST]+)L|ST([ST]+)L|SL([ST]+)L|TS([ST]+)L|TT([ST]+)L|(TL)|(LL)))', ''.join(c for c in CODE if c in 'STL'), 64)
    )
    
    any(c>-1 and
        PCs.append( 
          eval( Operations[I[c][0]].format(
            L.get(I[c][1]) if I[c][0]>2 else
              eval('+-'[I[c][1][0]!='S']+'0b'+I[c][1][1:].translate({83:48,84:49})),
            ) + ( I[c][0]<17 and ' or c+1' or '' )
          )
        )
      for c in PCs)
    
    return ''.join(result)


if __name__=='__main__':
  n = 25; print(n, CCCCCCC(n))
  n = 13; print(n, CCCCCCC(n))
  n = 10; print(n, CCCCCCC(n))
  n = 16; print(n, CCCCCCC(n))
