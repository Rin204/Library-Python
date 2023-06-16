# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.Combination import Combination


T, MOD = map(int, input().split())
# 勝手にテーブルを拡張してくれるテスト
C = Combination(min(MOD - 1, 100000), MOD)

for _ in range(T):
    n, k = map(int, input().split())
    print(C.nCk(n, k))
