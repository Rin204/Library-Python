# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.math.MillerRabin import MillerRabin

Q = int(input())
for _ in range(Q):
    n = int(input())
    if MillerRabin(n):
        print("Yes")
    else:
        print("No")
