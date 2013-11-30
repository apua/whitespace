def run(code):

  global PCs, CPSR, Stack, Labels, Heap, num, putchar, getchar

  Stack = []
  Heap = {}

  patt = r'''(?:
    S (?:
      S ([ST]{2,})L|
      TS([ST]{2,})L|
      TL([ST]{2,})L|
      (LS)|
      (LT)|
      (LL) )|
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
    )
  '''

  Labels = {}
  Instructions = []
  PCs = [0]
  CPSR = []

  putchar = lambda u,o=__import__('sys').stdout: o.write(u) and o.flush()
  getchar = lambda: __import__('sys').stdin.read(1)
  num = lambda n: eval('+-'[n[0]!='S']+'0b'+n[1:].translate({83:48,84:49}))
  Operations = [
    # stack manipulation
    (lambda n,c: eval( 'Stack.append({n}) or {c}+1'.format(n=num(n),c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Stack[-{n}]) or {c}+1'.format(n=num(n),c=c) ) ),
    (lambda n,c: eval( 'any(Stack.pop(-2) and 0 for t in range({n})) or {c}+1'.format(n=num(n),c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Stack[-1]) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.insert(-1,Stack.pop()) or  {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.pop() and 0 or {c}+1'.format(n=n,c=c) ) ),
    # arithmetic
    (lambda n,c: eval( 'Stack.append(Stack.pop(-2)+Stack.pop()) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Stack.pop(-2)-Stack.pop()) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Stack.pop(-2)*Stack.pop()) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Stack.pop(-2)//Stack.pop()) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Stack.pop(-2)%Stack.pop()) or {c}+1'.format(n=n,c=c) ) ),
    # heap
    (lambda n,c: eval( 'Heap.__setitem__(Stack.pop(-2), Stack.pop()) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Stack.append(Heap.__getitem__(Stack.pop())) or {c}+1'.format(n=n,c=c) ) ),
    # IO
    (lambda n,c: eval( 'putchar(chr(Stack.pop())) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'putchar(str(Stack.pop())) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Heap.__setitem__(Stack.pop(),ord(getchar())) or {c}+1'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'Heap.__setitem__(Stack.pop(),int(input())) or {c}+1'.format(n=n,c=c) ) ),
    # flow
    (lambda n,c: eval( '0'.format(n=n,c=c) ) ),
    (lambda n,c: eval( 'CPSR.append({c}+1) or {n}'.format(n=Labels[n],c=c) ) ),
    (lambda n,c: eval( '{n}'.format(n=Labels[n],c=c) ) ),
    (lambda n,c: eval( '{n} if Stack.pop()==0 else {c}+1'.format(n=Labels[n],c=c) ) ),
    (lambda n,c: eval( '{n} if Stack.pop()<0 else {c}+1'.format(n=Labels[n],c=c) ) ),
    (lambda n,c: eval( 'CPSR.pop()'.format(n=n,c=c) ) ),
    (lambda n,c: eval( '-1'.format(n=n,c=c) ) ),
  ]
  
  any(
    any( Instructions.append((p,v)) if p!=17 else Labels.__setitem__(v, len(Instructions))
      for p,v in enumerate(m.groups()) if v )
    for m in __import__('re').finditer(patt, code, 64)
  )

  any(c>-1 and PCs.append( Operations[Instructions[c][0]](Instructions[c][1],c) )
    for c in PCs) #or result


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
