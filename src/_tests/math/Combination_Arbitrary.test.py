# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.CombinationArbitrary import CombinationArbitrary


T, MOD = map(int, input().split())
Comb = CombinationArbitrary(MOD)
for _ in range(T):
    n, k = map(int, input().split())
    print(Comb.nCk(n, k))
