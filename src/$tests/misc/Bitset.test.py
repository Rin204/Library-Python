# verification-helper: PROBLEM https://yukicoder.me/problems/no/1861
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.misc.Bitset import Bitset
from copy import deepcopy

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = int(n**0.5)
bs = Bitset(k + 1)
bs[0] = 1
dp = [deepcopy(bs)]
for i, a in enumerate(A, 1):
    bs |= bs << a
    if i % B == 0:
        dp.append(deepcopy(bs))

if not bs[k]:
    print(-1)
    exit()

bit = Bitset(k + 1)
bit[k] = 1
ans = 0

p = (n - 1) // B
dp2 = [dp[p]]
for i in range(B * p, n - 1):
    dp2.append(dp2[-1] | (dp2[-1] << A[i]))

for i in range(n - 1, -1, -1):
    if bit.and_count(dp2[i % B]) == 0:
        ans += 1
    if i % B == 0:
        p = (i - 1) // B
        dp2 = [dp[p]]
        for j in range(B * p, B * (p + 1) - 1):
            dp2.append(dp2[-1] | (dp2[-1] << A[j]))
    bit |= bit >> A[i]

print(ans)
