# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.convolution.and_convolution import and_convolution


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = and_convolution(A, B, 998244353)
print(*C)
