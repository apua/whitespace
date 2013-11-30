def run(code):

  global CPSR, Stack, Heap, putchar, getchar

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
    'putchar(chr(Stack.pop()))',
    'putchar(str(Stack.pop()))',
    'Heap.__setitem__(Stack.pop(),ord(getchar()))',
    'Heap.__setitem__(Stack.pop(),int(input()))',
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
    any( Instructions.append((p,v)) if p!=17 else Labels.__setitem__(v, len(Instructions))
      for p,v in enumerate(m.groups()) if v )
    for m in __import__('re').finditer(patt, code, 64)
  )

  any(c>-1 and
      PCs.append( 
        eval( Operations[Instructions[c][0]].format(
          Labels.get(Instructions[c][1]) if Instructions[c][0]>2 else num(Instructions[c][1]) ,
          ) + ( Instructions[c][0]<17 and ' or c+1' or '' )
        )
      )
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
