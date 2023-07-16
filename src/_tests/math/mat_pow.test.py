# verification-helper: PROBLEM https://yukicoder.me/problems/no/1750
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.mat_exp import mat_exp

n, m, T = map(int, input().split())
A = [[0] * n for _ in range(n)]
B = [0] * n
B[0] = 1
for _ in range(m):
    s, t = map(int, input().split())
    A[s][t] = 1
    A[t][s] = 1

B = mat_exp(A, B, T, 998244353)
print(B[0])
