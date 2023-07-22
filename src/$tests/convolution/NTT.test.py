# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.convolution.NTT import NTT


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ntt = NTT()
C = ntt.multiply(A, B)
print(*C)
