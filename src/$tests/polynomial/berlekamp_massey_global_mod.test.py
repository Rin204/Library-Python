# verification-helper: PROBLEM https://judge.yosupo.jp/problem/find_linear_recurrence
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.polynomial.berlekamp_massey_global_mod import berlekamp_massey_global_mod


n = int(input())
if n == 0:
    A = []
else:
    A = list(map(int, input().split()))
C = berlekamp_massey_global_mod(A)
print(len(C))
print(*C)
