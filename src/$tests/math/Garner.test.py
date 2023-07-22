# verification-helper: PROBLEM https://yukicoder.me/problems/no/187
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.Garner import Garner


n = int(input())
R = [0] * n
M = [0] * n
for i in range(n):
    R[i], M[i] = map(int, input().split())

r, m = Garner(R, M)
if r == -1:
    print(-1)
else:
    if r == 0:
        r = m
    print(r % (10**9 + 7))
