# verification-helper: PROBLEM https://yukicoder.me/problems/no/1750
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
MOD = 998244353


def mat_exp_global_mod(A, B, n):
    le = len(A)
    while n > 0:
        if n & 1:
            C = [0] * le
            for i in range(le):
                for j in range(le):
                    C[i] += A[i][j] * B[j]
                    C[i] %= MOD
            B = C
        C = [[0] * le for _ in range(le)]
        for i in range(le):
            for k in range(le):
                for j in range(le):
                    C[i][j] += A[i][k] * A[k][j]
                    C[i][j] %= MOD
        A = C
        n >>= 1

    return B


n, m, T = map(int, input().split())
A = [[0] * n for _ in range(n)]
B = [0] * n
B[0] = 1
for _ in range(m):
    s, t = map(int, input().split())
    A[s][t] = 1
    A[t][s] = 1

B = mat_exp_global_mod(A, B, T)
print(B[0])
