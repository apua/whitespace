======================
Whitespace Interpreter
======================

Goal 目標
=========

Building a simple Whitespace interpreter in Python
to interpret polyglot (with Python and Whitespace).

用 Python 實作 Whitespace 直譯器以用於混合 Python 與 Whitespace 的程式.

~~~~

Using Python3.x to implement because Python3.x is better than Python2.x .

使用 Python3.x , 因為比較理想比較好寫一行文...

~~~~

The lexical tokens (``' \t\n'``) could be modified to something like
``'\u0020\u2000\3000'`` or ``'STL'``. So, there should be a factory
(which might be a function or class) to generate interpreter
(which might be a function or class) with different lexical tokens.

要提供根據指定的 lexical tokens 跑直譯器; 可能需要用 factory 生成直譯器.

~~~~

Input and Output could be modified for embedding Python program
like this::

    def f(*arg):
        ws_code = '[STL]+'
        def run_ws(code, arg=args): pass
        return run_ws(ws_code, *args)
    
So, input might read from an argument buffer, and output might store to
a result buffer which would be return when interpreter terminates.

Whitespace 的 input/output 要視狀況調整 (how?) ;
在內嵌於 Python code 宛如一道 function 的狀態時, 必須能吃參數和回傳結果,
應該會用各提供一套 buffer 的方式來實作.

~~~~

The Python code of interpreter would be combined to one line and still simple,
so some syntax like ``def`` or ``del`` would not be used.

要盡可能保持精簡和轉一行文的可能性; 演算法仍要有一定程度的效率, 不能有不必要的重複計算.

