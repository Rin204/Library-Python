# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
MOD = 998244353


def and_convolution_global_mod(A, B):
    n = max(len(A), len(B))
    l = (n - 1).bit_length()
    n = 1 << l
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))

    def f(A):
        for i in range(l):
            for bit in range(n):
                if not bit >> i & 1:
                    A[bit] += A[bit ^ (1 << i)]
                    A[bit] %= MOD

    def invf(A):
        for i in range(l):
            for bit in range(n):
                if not bit >> i & 1:
                    A[bit] -= A[bit ^ (1 << i)]
                    A[bit] %= MOD

    f(A)
    f(B)
    C = [a * b % MOD for a, b in zip(A, B)]
    invf(C)
    return C


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = and_convolution_global_mod(A, B)
print(*C)
