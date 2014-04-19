# -*- coding=utf8 -*-

'''
usage:
    $ py3 wvm.py $FILE [ $LEXICAL_TOKEN ]

doctest::
>>> code = """
... SSSTL
... LSSSTSS SSTTL
... SLS
... TLST
... SSSTSTSL
... TLSS
... SSSTL
... TSSS
... SLS
... SSSTSTTL
... TSST
... LTSSTSS STSTL
... LSLSTS SSSTTL
... LSSSTS SSTSTL
... SLL
... LLL
... """
>>> run_wvm(code)
'''

def run_wvm(whitespace_code, lexical_token='STL'):
    '''compile Whitespace code and run VM'''

    import re
    from pprint import pprint as p

    def clean(code, token=lexical_token):
        return ''.join(c for c in code if c in token)#.translate()

    W = clean(whitespace_code)

    # 根據 instruction set 定義 pattern
    T = instruction_translate= (
        {'pattern': r'SS([ST][ST]+)L',  'IR': 'Stack.append({})'},
        {'pattern': r'STS([ST][ST]+)L', 'IR': 'Stack.append(Stack[-{}])'                    },
        {'pattern': r'STL([ST][ST]+)L', 'IR': 'any(Stack.pop(-2) and 0 for t in range({}))' },
        {'pattern': r'SLS()',           'IR': 'Stack.append(Stack[-1])'                     },
        {'pattern': r'SLT()',           'IR': 'Stack.insert(-1,Stack.pop())'                },
        {'pattern': r'SLL()',           'IR': 'Stack.pop() and 0'                           },
        {'pattern': r'TSSS()',          'IR': 'Stack.append(Stack.pop(-2)+Stack.pop())'     },
        {'pattern': r'TSST()',          'IR': 'Stack.append(Stack.pop(-2)-Stack.pop())'     },
        {'pattern': r'TSSL()',          'IR': 'Stack.append(Stack.pop(-2)*Stack.pop())'     },
        {'pattern': r'TSTS()',          'IR': 'Stack.append(Stack.pop(-2)//Stack.pop())'    },
        {'pattern': r'TSTT()',          'IR': 'Stack.append(Stack.pop(-2)%Stack.pop())'     },
        {'pattern': r'TTS()',           'IR': 'Heap.__setitem__(Stack.pop(-2), Stack.pop())'},
        {'pattern': r'TTT()',           'IR': 'Stack.append(Heap.__getitem__(Stack.pop()))' },
        {'pattern': r'TLSS()',          'IR': 'putchar(chr(Stack.pop()))'                   },
        {'pattern': r'TLST()',          'IR': 'putchar(str(Stack.pop()))'                   },
        {'pattern': r'TLTS()',          'IR': 'Heap.__setitem__(Stack.pop(),ord(getchar()))'},
        {'pattern': r'TLTT()',          'IR': 'Heap.__setitem__(Stack.pop(),int(input()))'  },
        {'pattern': r'LSS([ST]+)L',     'IR': '# set label'                                 },
        {'pattern': r'LST([ST]+)L',     'IR': 'CPSR.append(c+1) or {}'                      },
        {'pattern': r'LSL([ST]+)L',     'IR': '{}'                                          },
        {'pattern': r'LTS([ST]+)L',     'IR': '{} if Stack.pop()==0 else c+1'               },
        {'pattern': r'LTT([ST]+)L',     'IR': '{} if Stack.pop()<0 else c+1'                },
        {'pattern': r'LTL()',           'IR': 'CPSR.pop()'                                  },
        {'pattern': r'LLL()',           'IR': '-1'                                          },
        )

    # 這段會把轉譯的 IR 建立出來, 並設定 label
    I = intermediate_representation = []
    R = pattern = '|'.join(t['pattern'] for t in T)
    L = temporary_label_mapping = {}
    for match in re.finditer(R,W,re.VERBOSE):
        for k, v in enumerate(match.groups()):
            if v is not None:
                if T[k]['IR']=='# set label':
                    L[v] = len(I)
                else:
                    I.append((T[k]['IR'], v))
                break
    p(L)
    p(list(enumerate(I)))
                
    S = stack = []
    H = heap = {}
    P = program_counter = 0
    run = lambda :None


def get_argvs():
    import sys
    argvs = {'whitespace_code': open(sys.argv[1]).read() ,
             'lexical_token': ' \t\n' if len(sys.argv[1])<3 else sys.argv[2]}
    return argvs


if __name__=='__main__':
    import doctest
    run_wvm(**get_argvs())
