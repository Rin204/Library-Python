# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_primes
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.EnumeratePrimes import EnumeratePrimes


n, a, b = map(int, input().split())
primes = EnumeratePrimes(n)
le = len(primes)
ans = []
for i in range(b, le, a):
    ans.append(primes[i])

print(le, len(ans))
print(*ans)
