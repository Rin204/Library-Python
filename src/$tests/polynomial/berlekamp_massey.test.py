# verification-helper: PROBLEM https://judge.yosupo.jp/problem/find_linear_recurrence
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.polynomial.berlekamp_massey import berlekamp_massey


n = int(input())
if n == 0:
    A = []
else:
    A = list(map(int, input().split()))
C = berlekamp_massey(A, 998244353)
print(len(C))
print(*C)
