# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.convolution.or_convolution_global_mod import or_convolution_global_mod


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_ = [0] * (1 << n)
B_ = [0] * (1 << n)
mask = (1 << n) - 1
for i in range(1 << n):
    A_[i ^ mask] = A[i]
    B_[i ^ mask] = B[i]
C_ = or_convolution_global_mod(A_, B_)
C = [0] * (1 << n)
for i in range(1 << n):
    C[i ^ mask] = C_[i]
print(*C)
