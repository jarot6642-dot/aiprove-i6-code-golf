# Session transcript — aiprove-i6-code-golf

Date: Sat 2026-11-14 11:37 WIB (04:37 UTC). Environment: Linux x86_64, Python 3.12.3.
Author handle for this work: BrightAgent. No secrets were used or printed in this session.

## Commands run

```
$ wc -c entry.py
$ python3 test_expr.py
```

## Output

```
149 entry.py
PASS  '2+3*4' -> 14 (expected 14)
PASS  '(2+3)*4' -> 20 (expected 20)
PASS  '-5+3' -> -2 (expected -2)
PASS  '10/4' -> 2.5 (expected 2.5)
PASS  '2*-3' -> -6 (expected -6)
PASS  '((1+2)*(3+4))/2' -> 10.5 (expected 10.5)
PASS  '1+2+3+4+5' -> 15 (expected 15)
PASS  '100/10/2' -> 5.0 (expected 5.0)
PASS  '-(3+2)' -> -5 (expected -5)
PASS  '3.5*2' -> 7.0 (expected 7.0)
PASS  '0' -> 0 (expected 0)
PASS  ' 2 + 3 ' -> 5 (expected 5)
PASS  '7-10' -> -3 (expected -3)
PASS  '2*(3+4*(5-2))' -> 30 (expected 30)
PASS  '1/3' -> 0.3333333333333333 (expected 0.3333333333333333)
PASS  '10-2*3' -> 4 (expected 4)
PASS  '(8/2)/(2/1)' -> 2.0 (expected 2.0)
PASS  '-(-4)' -> 4 (expected 4)
PASS  '123+456' -> 579 (expected 579)
PASS  '2.5+2.5' -> 5.0 (expected 5.0)
PASS  rejected: '2**3'
PASS  rejected: '10//3'
PASS  rejected: 'import os'
PASS  rejected: "__import__('os')"
PASS  rejected: '2+abc'
PASS  rejected: ''
PASS  rejected: "os.system('id')"
PASS  rejected: '[1,2,3]'
PASS  rejected: '2;3'
PASS  rejected: 'lambda x: x'
PASS  rejected: '1e3+2'
FUZZ  500/500 random expressions agree with reference eval()
TOTAL  passed=531 failed=0
```

Exit code: 0.

## Summary

- Entry size: **149 bytes** (`entry.py`).
- Approach: strict regex validation + `eval()` with empty globals — no hand-written parser.
- Tests: 20 fixed cases pass, 11 rejected inputs rejected, 500/500 seeded fuzz expressions agree with the reference. Total passed=531, failed=0.
