======================
Whitespace Interpreter
======================

Goal 目標
=========

Building a simple Whitespace interpreter in Python
to interpret polyglot (with Python and Whitespace).

    用 Python 實作 Whitespace 直譯器以用於混合 Python 與 Whitespace 的程式.



Using Python3.x to implement because Python3.x is better than Python2.x .

    使用 Python3.x , 因為比較理想比較好寫一行文...



The lexical tokens (``' \t\n'``) could be modified to something like
``'\u0020\u2000\3000'`` or ``'STL'``. So, there should be a factory
(which might be a function or class) to generate interpreter
(which might be a function or class) with different lexical tokens.

    要提供根據指定的 lexical tokens 跑直譯器; 可能需要用 factory 生成直譯器.



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



The Python code of interpreter would be combined to one line and still simple,
so some syntax like ``def`` or ``del`` would not be used.

    要盡可能保持精簡和轉一行文的可能性; 演算法仍要有一定程度的效率, 不能有不必要的重複計算.

...

    應測試過官方網站的 `所有範例程式碼 <http://compsoc.dur.ac.uk/whitespace/examples.php>`_ ,
    盡可能確保直譯器是正確的
    
...

    有別於要嵌入的程式碼, 原始的直譯器程式應包含多種常用功能, 含轉檔 (轉成指定字元), 清檔 (清除不要的字),
    下載/存檔 (瀏覽器與複製貼上很容易掉資訊), 顯示編譯好的 operations (話說這還比較好讀!?)
    
...

    考慮到 debug 和開發, 有些工具/功能還蠻重要的, 例如列出 labels table/instructions/operations,
    即時呈現 PCs (Whitespace 允許 recursive subroutine) /Counters/Stacks/Heaps ...
    或許可做成 spreadsheet 比較好 trace?...(我是不是太超過了...)


Idea
====

*注意*: 

    當前的目標是整理出 **精簡的 compiler**, 而不是理想的 compiler

其他考慮 (如 debug):

* 改成 dict 來找各 operation, 避免用 list 而 index 不明確, 除此之外, 也讓 debug 好做
* 新增一個動作叫 clean(), 在程式結束時做清理
* 做成 class 可能比較好設值?
* 跑兩遍來換掉 number

- Stack
- Heap

- INSTRUCTION_PATTERN

- Lables
- Instructions
- PCs
  | program counter in list

- not_label
  | return True if not lable else set_lable and False)

