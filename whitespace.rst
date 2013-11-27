::

  S   S   STL             Put a 1 on the stack
  L   SS  STSSSSTTL       Set a Label at this point
  S   LS                  Duplicate the top stack item
  TL  ST                  Output the current value
  S   S   STSTSL          Put 10 (newline) on the stack...
  TL  SS                  ...and output the newline
  S   S   STL             Put a 1 on the stack
  TS  SS                  Addition. This increments our current value.
  S   LS                  Duplicate that value so we can test it
  S   S   STSTTL          Push 11 onto the stack
  TS  ST                  Subtraction. So if we've reached the end, we have a zero on the stack.
  L   TS  STSSSTSTL       If we have a zero, jump to the end
  L   SL  STSSSSTTL       Jump to the start
  L   SS  STSSSTSTL       Set the end label
  S   LL                  Discard our accumulator, to be tidy
  L   LL                  Finish

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======= == =====================
S stack manipulation
--------------------------------
    S   n   push
    LS      copy 1st item
    TS  n   copy nth item
    LT      swap top 2 items
    LL      drop 1st item
    TL  n   drop 2nd~n+1th items
======= == =====================

======= == =====================
TS arithmetic
--------------------------------
    SS      \+
    ST      \-
    SL      \*
    TS      /
    TT      %
======= == =====================

======= == =====================
TT heap
--------------------------------
    S       store
    T       retrieve
======= == =====================

======= == =====================
L flow
--------------------------------
    SS  l   mark
    ST  l   call subroutine
    SL  l   jump
    TS  l   jump if 0
    TT  l   jump if negative
    TL      end subroutine
    LL      end program
======= == =====================

======= == =====================
TL IO
--------------------------------
    SS      %c
    ST      %d
    TS      &c
    TT      &d
======= == =====================


