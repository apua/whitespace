def run(code):

  Stack = []
  Heap = {}

  patt = r'''(?:
    S (?:
      S ([ST]{2,})L|
      (LS)|
      TS([ST]{2,})L|
      (LT)|
      (LL)|
      TL([ST]{2,})L) )|
    TS(?:
      (SS)|(ST)|(SL)|(TS)|(TT) )|
    TT(?:
      (S)|(T) )|
    TL(?:
      (SS)|(ST)|(TS)|(TT) )|
    L (?:
      SS([ST]+)L|
      ST([ST]+)L|
      SL([ST]+)L|
      TS([ST]+)L|
      TT([ST]+)L|
      (TL)|
      (LL) )
  '''
  debug = (lambda s:
           #print("  CPSR -> {}".format(CPSR)) or
           #print(" stack -> {}".format(Stack)) or
           #print(" heap -> {}".format(Heap)) or
           ##print(" labels -> {}".format(Labels)) or
           #print("PCs -> {}".format(PCs[-10:])) or
           #print(s) or 
           0)

  Labels = {}
  Instructions = []
  PCs = [0]
  CPSR = []

  num = lambda n: eval('+-'[n[0]!='S']+'0b'+n[1:].translate({83:48,84:49}))
  Operations = [
    # stack manipulation
    (lambda n,c: 
     Stack.append(num(n)) or
     PCs.append(c+1) or 
     debug('push') or
     0),
    (lambda n,c: 
     Stack.append(Stack[-1]) or
     PCs.append(c+1) or 
     debug('copy 1th item') or 
     0),
    (lambda n,c: 
     Stack.append(Stack[-num(n)]) or
     PCs.append(c+1) or 
     debug('copy nth item') or 
     0),
    (lambda n,c:
     Stack.insert(-1,Stack.pop()) or 
     PCs.append(c+1) or 
     debug('swap top 2 items') or 
     0),
    (lambda n,c:
     Stack.__delitem__(-1) or
     PCs.append(c+1) or 
     debug('drop top item') or 
     0),
    (lambda n,c:
     any(Stack.__delitem__(-2) for t in range(n)) or
     PCs.append(c+1) or 
     debug('drop [-n-1:-1] items') or 
     0),
    # arithmetic
    (lambda n,c:
     Stack.append(Stack.pop()+Stack.pop()) or
     PCs.append(c+1) or 
     debug('+') or 
     0),
    (lambda n,c:
     Stack.append(Stack.pop(-2)-Stack.pop()) or
     PCs.append(c+1) or 
     debug('-') or
     0),
    (lambda n,c:
     Stack.append(Stack.pop()*Stack.pop()) or
     PCs.append(c+1) or 
     debug('*') or 
     0),
    (lambda n,c:
     Stack.append(Stack.pop()//Stack.pop()) or
     PCs.append(c+1) or 
     debug('/') or 
     0),
    (lambda n,c:
     Stack.append(Stack.pop()%Stack.pop()) or
     PCs.append(c+1) or 
     debug('%') or 
     0),
    # heap
    (lambda n,c:
     Heap.__setitem__(Stack.pop(-2), Stack.pop()) or
     PCs.append(c+1) or 
     debug('store') or 
     0),
    (lambda n,c:
     Stack.append(Heap.__getitem__(Stack.pop())) or
     PCs.append(c+1) or 
     debug('retrieve') or 
     0),
    # IO
    (lambda n,c:
     __import__('sys').stdout.write(chr(Stack.pop())) and
     __import__('sys').stdout.flush() or 
     PCs.append(c+1) or
     debug('%c') or
     0),
    (lambda n,c:
     __import__('sys').stdout.write(str(Stack.pop())) and 
     __import__('sys').stdout.flush() or 
     PCs.append(c+1) or
     debug('%d') or 
     0),
    (lambda n,c:
     Heap.__setitem__(Stack.pop(),ord(__import__('sys').stdin.read(1))) or
     PCs.append(c+1) or
     debug('&c') or 
     0),
    (lambda n,c:
     Heap.__setitem__(Stack.pop(),int(input())) or
     PCs.append(c+1) or
     debug('%d') or 
     0),
    # flow
    (lambda n,c: 0),
    (lambda n,c:
     PCs.append(CPSR.append(c+1) or Labels[n]) or
     debug('call subroutine') or 
     0),
    (lambda n,c:
     PCs.append(Labels[n]) or
     debug('jump') or 
     0),
    (lambda n,c:
     PCs.append(Labels[n] if Stack.pop()==0 else c+1 ) or 
     debug('jump if 0') or 
     0),
    (lambda n,c:
     PCs.append(Labels[n] if Stack.pop()<0 else c+1 ) or 
     debug('jump if negative') or 
     0),
    (lambda n,c:
     PCs.append(CPSR.pop()) or
     debug('end subroutine') or 
     0),
    (lambda n,c:
     PCs.append(-1) or 
     #any(PCs.pop() and 0 for c in range(len(PCs))) or
     debug('end program') or 
     0),
  ]
  
  any(Instructions.append(m.groups())
    for m in __import__('re').finditer(patt, code, 64)
      if not m.group(18) or Labels.__setitem__(m.group(18),len(Instructions))
  )

  any(
    any(Instructions.__setitem__(i,Operations[j].__get__(v))
        for j,v in enumerate(T) if v)
    for i,T in enumerate(Instructions)
  )

  any(c>-1 and Instructions[c](c) for c in PCs) #or result


if __name__=='__main__':
  from sys import argv, stdin
  from ws_trans import clean_content
  if len(argv)>1:
    code = open(argv[1]).read()
  else:
    code = stdin.read()
  code = clean_content(code,'STL')
  #print(code)
  run(code)
