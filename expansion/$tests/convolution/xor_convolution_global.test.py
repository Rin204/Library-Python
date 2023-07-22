# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
MOD = 998244353


def xor_convolution_global_mod(A, B):
    n = max(len(A), len(B))
    l = (n - 1).bit_length()
    n = 1 << l
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))

    def f(A):
        h = 1
        while h < len(A):
            for i in range(0, len(A), h * 2):
                for j in range(i, i + h):
                    x = A[j]
                    y = A[j + h]
                    A[j] = (x + y) % MOD
                    A[j + h] = (x - y) % MOD
            h *= 2

    f(A)
    f(B)
    C = [a * b % MOD for a, b in zip(A, B)]
    f(C)
    inv = pow(n, MOD - 2, MOD)
    return [c * inv % MOD for c in C]


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = xor_convolution_global_mod(A, B)
print(*C)
