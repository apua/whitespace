def run(code):

  Stack = []
  Heap = {}

  INSTRUCTION_PATTERN = patt = r'''(?:
    S (?:
      S ([ST]{2,})L|
      LS()|
      TS([ST]{2,})L|
      LT()|
      LL()|
      TL([ST]{2,})L) )|
    TS(?:
      SS()|ST()|SL()|TS()|TT() )|
    TT(?:
      S()|T() )|
    L (?:
      SS([ST]+)L|
      ST([ST]+)L|
      SL([ST]+)L|
      TS([ST]+)L|
      TT([ST]+)L|
      TL()|
      LL() )|
    TL(?:
      SS()|ST()|TS()|TT() )
  '''
  verbose_output = debug = (lambda s:
           #print("  CPSR -> {}".format(CPSR)) or
           #print(" stack -> {}".format(Stack)) or
           #print(" heap -> {}".format(Heap)) or
           ##print(" labels -> {}".format(Labels)) or
           #print("counters -> {}".format(Counters[-10:])) or
           #print(s) or 
           0)

  Labels = {}
  Instructions = []
  PCs = CPSR = []

  num = lambda n: eval('+-'[n[0]!='S']+'0b'+n[1:].translate({83:48,84:49}))
  Counters = [0]
  Operations = [
    # stack manipulation
    (lambda n: 
     Stack.append(num(n)) or
     Counters.append(c+1) or 
     debug('push') or
     0),
    (lambda n: 
     Stack.append(Stack[-1]) or
     Counters.append(c+1) or 
     debug('copy 1th item') or 
     0),
    (lambda n: 
     Stack.append(Stack[-num(n)]) or
     Counters.append(c+1) or 
     debug('copy nth item') or 
     0),
    (lambda n:
     Stack.insert(-1,Stack.pop()) or 
     Counters.append(c+1) or 
     debug('swap top 2 items') or 
     0),
    (lambda n:
     Stack.__delitem__(-1) or
     Counters.append(c+1) or 
     debug('drop top item') or 
     0),
    (lambda n:
     any(Stack.__delitem__(-2) for t in range(n)) or
     Counters.append(c+1) or 
     debug('drop [-n-1:-1] items') or 
     0),
    # arithmetic
    (lambda n:
     Stack.append(Stack.pop()+Stack.pop()) or
     Counters.append(c+1) or 
     debug('+') or 
     0),
    (lambda n:
     Stack.append(Stack.pop(-2)-Stack.pop()) or
     Counters.append(c+1) or 
     debug('-') or
     0),
    (lambda n:
     Stack.append(Stack.pop()*Stack.pop()) or
     Counters.append(c+1) or 
     debug('*') or 
     0),
    (lambda n:
     Stack.append(Stack.pop()//Stack.pop()) or
     Counters.append(c+1) or 
     debug('/') or 
     0),
    (lambda n:
     Stack.append(Stack.pop()%Stack.pop()) or
     Counters.append(c+1) or 
     debug('%') or 
     0),
    # heap
    (lambda n:
     Heap.__setitem__(Stack.pop(-2), Stack.pop()) or
     Counters.append(c+1) or 
     debug('store') or 
     0),
    (lambda n:
     Stack.append(Heap.__getitem__(Stack.pop())) or
     Counters.append(c+1) or 
     debug('retrieve') or 
     0),
    # flow
    (lambda n:
     Labels.__setitem__(n,len(Instructions)) or
     debug('mark') or
     0),
    (lambda n:
     Counters.append(Labels[n]) or
     #not CPSR and CPSR.append(c+1) or 
     CPSR.append(c+1) or
     debug('call subroutine') or 
     0),
    (lambda n:
     Counters.append(Labels[n]) or
     debug('jump') or 
     0),
    (lambda n:
     Counters.append(Labels[n] if Stack.pop()==0 else c+1 ) or 
     debug('jump if 0') or 
     0),
    (lambda n:
     Counters.append(Labels[n] if Stack.pop()<0 else c+1 ) or 
     debug('jump if negative') or 
     0),
    (lambda n:
     Counters.append(CPSR.pop()) or
     debug('end subroutine') or 
     0),
    (lambda n:
     any(Counters.pop() and 0 for c in range(len(Counters))) or
     debug('end program') or 
     0),
    # IO
    (lambda n:
     __import__('sys').stdout.write(chr(Stack.pop())) and
     __import__('sys').stdout.flush() or 
     Counters.append(c+1) or
     debug('%c') or
     0),
    (lambda n:
     __import__('sys').stdout.write(str(Stack.pop())) and 
     __import__('sys').stdout.flush() or 
     Counters.append(c+1) or
     debug('%d') or 
     0),
    (lambda n:
     Heap.__setitem__(Stack.pop(),ord(__import__('sys').stdin.read(1))) or
     Counters.append(c+1) or
     debug('&c') or 
     0),
    (lambda n:
     Heap.__setitem__(Stack.pop(),int(input())) or
     Counters.append(c+1) or
     debug('%d') or 
     0),
  ]
  
  not_label = lambda v: Labels.__setitem__(v,len(Instructions)) if v else True
  any(
    any(Instructions.append(Operations[i].__get__(v))
        for i,v in enumerate(m.groups(0)) if v!=0)
    for m in __import__('re').finditer(patt, code, 64)
      if not_label(m.group(14)) #24
  )

  for c in Counters: Instructions[c]()
  # run and end
  #any(c=='END' or run(c) for c in PCs) and result


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
