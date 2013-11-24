======================
Whitespace Interpreter
======================

Goal
----

Building a simple Whitespace interpreter in Python
to interpret polyglot (with Python and Whitespace).

Using Python3.x to implement because Python3.x is better than Python2.x .

The lexical tokens (``' \t\n'``) could be modified to something like
``'\u0020\u2000\3000'`` or ``'STL'``. So, there should be a factory
(which might be a function or class) to generate interpreter
(which might be a function or class) with different lexical tokens.

Input and Output could be modified for embedding Python program
like this::

    def f(*arg):
        ws_code = '[STL]+'
        def run_ws(code, arg=args): pass
        return run_ws(ws_code, *args)
        
So, input might read from an argument buffer, and output might store to
a result buffer which would be return when interpreter terminates.

The Python code of interpreter would be combined to one line and still simple,
so some syntax like ``def`` or ``del`` would not be used.


    
