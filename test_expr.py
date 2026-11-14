"""Tests + fuzz for entry.py (the 149-byte eval-based evaluator)."""
import random
import sys

from entry import e

CASES = [
    ("2+3*4", 14),
    ("(2+3)*4", 20),
    ("-5+3", -2),
    ("10/4", 2.5),
    ("2*-3", -6),
    ("((1+2)*(3+4))/2", 10.5),
    ("1+2+3+4+5", 15),
    ("100/10/2", 5.0),
    ("-(3+2)", -5),
    ("3.5*2", 7.0),
    ("0", 0),
    (" 2 + 3 ", 5),
    ("7-10", -3),
    ("2*(3+4*(5-2))", 30),
    ("1/3", 1 / 3),
    ("10-2*3", 4),
    ("(8/2)/(2/1)", 2.0),
    ("-(-4)", 4),
    ("123+456", 579),
    ("2.5+2.5", 5.0),
]

REJECTED = ["2**3", "10//3", "import os", "__import__('os')", "2+abc", "",
            "os.system('id')", "[1,2,3]", "2;3", "lambda x: x", "1e3+2"]

def main():
    passed = failed = 0
    for expr, expected in CASES:
        try:
            got = e(expr)
            ok = got == expected
        except Exception as exc:  # noqa: BLE001
            got, ok = f"{type(exc).__name__}: {exc}", False
        print(f"{'PASS' if ok else 'FAIL'}  {expr!r} -> {got} (expected {expected})")
        passed += ok
        failed += not ok

    for expr in REJECTED:
        try:
            got = e(expr)
            print(f"FAIL  rejected-case accepted: {expr!r} -> {got}")
            failed += 1
        except ValueError:
            print(f"PASS  rejected: {expr!r}")
            passed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL  rejected-case wrong error: {expr!r} -> {type(exc).__name__}")
            failed += 1

    # Fuzz: random well-formed expressions, checked against plain eval().
    rng = random.Random(20261114)
    fuzz_ok = 0
    for _ in range(500):
        n = rng.randint(1, 4)
        parts = []
        for _ in range(n):
            parts.append(str(rng.randint(0, 99)))
            if rng.random() < 0.3:
                parts.append(f".{rng.randint(0, 9)}")
            parts.append(rng.choice(["+", "-", "*", "/"]))
        expr = "".join(parts[:-1])
        if rng.random() < 0.4:
            expr = f"({expr})"
        if rng.random() < 0.2:
            expr = f"-({expr})"
        try:
            expected = eval(expr, {})  # noqa: S307 - reference oracle on generated input
            got = e(expr)
            assert got == expected, f"{expr}: {got} != {expected}"
            fuzz_ok += 1
        except ZeroDivisionError:
            fuzz_ok += 1  # both sides raise on /0; e() propagates it
        except AssertionError:
            print(f"FAIL  fuzz: {expr!r}")
            failed += 1
    print(f"FUZZ  {fuzz_ok}/500 random expressions agree with reference eval()")
    passed += fuzz_ok

    print(f"TOTAL  passed={passed} failed={failed}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
