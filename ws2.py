def run(code):

  global PCs, CPSR, Stack, Labels

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

  Labels = {}
  Instructions = []
  PCs = [0]
  CPSR = []

  num = lambda n: eval('+-'[n[0]!='S']+'0b'+n[1:].translate({83:48,84:49}))
  Operations = [
    # stack manipulation
    (lambda n,c: PCs.append(Stack.append(num(n)) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Stack[-1]) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Stack[-num(n)]) or c+1) ),
    (lambda n,c: PCs.append(Stack.insert(-1,Stack.pop()) or  c+1) ),
    (lambda n,c: PCs.append(Stack.__delitem__(-1) or c+1) ),
    (lambda n,c: PCs.append(any(Stack.__delitem__(-2) for t in range(n)) or c+1) ),
    # arithmetic
    (lambda n,c: PCs.append(Stack.append(Stack.pop(-2)+Stack.pop()) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Stack.pop(-2)-Stack.pop()) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Stack.pop(-2)*Stack.pop()) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Stack.pop(-2)//Stack.pop()) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Stack.pop(-2)%Stack.pop()) or c+1) ),
    # heap
    (lambda n,c: PCs.append(Heap.__setitem__(Stack.pop(-2), Stack.pop()) or c+1) ),
    (lambda n,c: PCs.append(Stack.append(Heap.__getitem__(Stack.pop())) or c+1) ),
    # IO
    (lambda n,c: PCs.append(__import__('sys').stdout.write(chr(Stack.pop())) and __import__('sys').stdout.flush() or c+1) ),
    (lambda n,c: PCs.append(__import__('sys').stdout.write(str(Stack.pop())) and __import__('sys').stdout.flush() or c+1) ),
    (lambda n,c: PCs.append(Heap.__setitem__(Stack.pop(),ord(__import__('sys').stdin.read(1))) or c+1) ),
    (lambda n,c: PCs.append(Heap.__setitem__(Stack.pop(),int(input())) or c+1) ),
    # flow
    (lambda n,c: 0),
    (lambda n,c: PCs.append(eval('CPSR.append({c}+1) or Labels["{n}"]'.format(n=n,c=c))) ),
    (lambda n,c: PCs.append(eval('Labels["{n}"]'.format(n=n,c=c))) ),
    (lambda n,c: PCs.append(eval('Labels["{n}"] if Stack.pop()==0 else {c}+1 '.format(n=n,c=c))) ),
    (lambda n,c: PCs.append(eval('Labels["{n}"] if Stack.pop()<0 else {c}+1 '.format(n=n,c=c))) ),
    (lambda n,c: PCs.append(eval('CPSR.pop()'.format(n=n,c=c))) ),
    (lambda n,c: PCs.append(eval('-1'.format(n=n,c=c))) ),
  ]
  
  any(
    any( Instructions.append((p,v)) if p!=17 else Labels.__setitem__(v, len(Instructions))
      for p,v in enumerate(m.groups()) if v )
    for m in __import__('re').finditer(patt, code, 64)
  )

  any(c>-1 and Operations[Instructions[c][0]](Instructions[c][1],c) 
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
