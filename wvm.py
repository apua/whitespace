# -*- coding=utf8 -*-

'''
usage:
    $ python wvm.py $FILE [ $LEXICAL_TOKEN ]
'''

def whitespace_interpreter(
    whitespace_code,
    lexical_token=' \t\n'):
    pass


def get_argvs():
    import sys
    argvs = {'whitespace_code': open(sys.argv[1]).read() ,
             'lexical_token': ' \t\n' if len(sys.argv[1])<3 else sys.argv[2]}
    return argvs


if __name__=='__main__':
    import doctest
    whitespace_interpreter(**get_argvs())
