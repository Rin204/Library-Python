# verification-helper: PROBLEM https://yukicoder.me/problems/no/1861
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.misc.Bitset import Bitset


n, k = map(int, input().split())
A = list(map(int, input().split()))
dp = [Bitset(k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i, a in enumerate(A, 1):
    dp[i] = dp[i - 1] | (dp[i - 1] << a)

if not dp[n][k]:
    print(-1)
    exit()

bit = Bitset(k + 1)
bit[k] = 1
ans = 0
for i in range(n - 1, -1, -1):
    a = A[i]
    if bit.and_count(dp[i]) == 0:
        ans += 1
    bit |= bit >> a
print(ans)
