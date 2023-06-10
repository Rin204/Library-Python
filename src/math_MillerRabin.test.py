# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test

from src.math.MillerRabin import MillerRabin

Q = int(input())
for _ in range(Q):
    n = int(input())
    if MillerRabin(n):
        print("Yes")
    else:
        print("No")
