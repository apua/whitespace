# -*- coding=utf8 -*-

'''
usage:
    $ python3 wvm.py $FILE [ $LEXICAL_TOKEN ]

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
    R = regex_pattern = r'''
        # S:=space, T:=tab, L:=Line Feed
        S (?: S ([ST][ST]+)L            |   # push n
              TS([ST][ST]+)L            |   # copy n-th item
              TL([ST][ST]+)L            |   # slide n items
              LS()                      |   # dup
              LT()                      |   # swap
              LL()                      )|  # drop
        TS(?: SS()|ST()|SL()|TS()|TT()  )|  # + - * // %
        TT(?: S ()|T ()                 )|  # store retrieve
        TL(?: SS()|ST()|TS()|TT() )|        # putchar putnum getchar getnum
        L (?: SS([ST]+)L                |   # set label
              ST([ST]+)L                |   # call subroutine
              SL([ST]+)L                |   # jump to label
              TS([ST]+)L                |   # jump to label if push ==0
              TT([ST]+)L                |   # jump to label if push < 0
              TL()                      |   # end subroutine
              LL()                      )   # end program
    '''
    p([match.groups() for match in re.finditer(R,W,re.VERBOSE)])
    S = stack = []
    H = heap = {}
    P = program_counter = 0
    T = text = []
    I = instruction_set = ()
    run = lambda :None


def get_argvs():
    import sys
    argvs = {'whitespace_code': open(sys.argv[1]).read() ,
             'lexical_token': ' \t\n' if len(sys.argv[1])<3 else sys.argv[2]}
    return argvs


if __name__=='__main__':
    import doctest
    run_wvm(**get_argvs())
