# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize

from src.math.PollardRho import primefact


Q = int(input())
for _ in range(Q):
    n = int(input())
    P = primefact(n)
    print(len(P), *P)
