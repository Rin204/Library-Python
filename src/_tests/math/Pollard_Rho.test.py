# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.math.PollardRho import primefact


Q = int(input())
for _ in range(Q):
    n = int(input())
    P = primefact(n)
    print(len(P), *P)
