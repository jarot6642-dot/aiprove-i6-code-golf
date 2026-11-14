# Tiny expression evaluator — code golf entry (149 bytes)

A tiny arithmetic expression evaluator in Python, golfed to **149 bytes**.

## Approach

Unlike a hand-written parser, this entry does **no parsing at all**. It
validates the input with a single strict character-class regex, then hands
the string to Python's own `eval()` with an empty globals dict:

1. `re.fullmatch('[0-9+*/(). -]+', s)` — only digits, `+ - * /`, parentheses,
   dots and spaces are allowed. No letters, no underscores, no brackets, no
   semicolons, so no names, attribute access, calls or imports can appear.
2. `'**' not in s and '//' not in s` — power and floor-division are excluded
   (they are not part of the required operator set).
3. `eval(s, {})` — with empty globals there is no `__builtins__` reachable
   from the expression, and step 1 already guarantees the string contains
   no identifiers anyway.

Anything that fails validation raises `ValueError('bad')`. Division by zero
propagates as `ZeroDivisionError`, exactly as in plain Python arithmetic.

## The entry (`entry.py`, 149 bytes)

```python
import re
def e(s):return eval(s,{})if re.fullmatch('[0-9+*/(). -]+',s)and'**'not in s and'//'not in s else (_ for _ in ()).throw(ValueError('bad'))
```

Usage:

```python
from entry import e
e("2+3*4")       # 14
e("(2+3)*4")     # 20
e("-5+3")        # -2
e("10/4")        # 2.5
e("2*-3")        # -6
e("2**3")        # ValueError: bad
e("import os")   # ValueError: bad
```

## Tests

```sh
python3 test_expr.py
```

Covers 20 fixed cases (arithmetic, parentheses, unary minus, division,
decimals, whitespace), 11 rejected inputs (power, floor-division, imports,
names, empty string), and a 500-case seeded fuzz run against plain `eval()`
as the reference oracle.

## Results

Run `python3 test_expr.py` — see `TRANSCRIPT.md` for the full log.
All fixed cases pass, all rejected inputs are rejected, and the fuzz run
agrees with the reference on 500/500 expressions.
