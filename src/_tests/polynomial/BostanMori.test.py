# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.convolution.NTT998 import NTT998
from src.polynomial.BostanMori998 import BostanMori998


d, k = map(int, input().split())
A = list(map(int, input().split()))
C = [1] + [-c for c in map(int, input().split())]
P = NTT998.multiply(A, C)
P = P[:d]
ans = BostanMori998(P, C, k)
print(ans)
