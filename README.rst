======================
Whitespace Interpreter
======================

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
