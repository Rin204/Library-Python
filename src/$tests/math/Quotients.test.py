# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_quotients
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.Quotients import Quotients


n = int(input())
res = Quotients(n)
print(len(res))
print(*[x for x, _, _ in res])
