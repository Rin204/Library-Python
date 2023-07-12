# verification-helper: PROBLEM https://yukicoder.me/problems/no/409
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.ConvexHullTrick import ConvexHullTrick


n, a, b, w = map(int, input().split())
D = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = w


ch = ConvexHullTrick()
for i, d in enumerate(D):
    ch.add_line(-2 * b * i, 2 * dp[i] + 2 * a * i + b * i * i + b * i)
    x = i + 1
    mi = ch.get(x)
    tmp = mi + 2 * a + 2 * d - 2 * a * x + b * x * x - b * x
    dp[x] = tmp // 2

ans = 1 << 60
for i in range(n + 1):
    d = n - i
    ans = min(ans, dp[i] - a * d + b * d * (d + 1) // 2)
print(ans)
