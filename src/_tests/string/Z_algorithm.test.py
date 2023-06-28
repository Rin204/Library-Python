# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.string.Z_algorithm import Z_algorithm

S = input()
res = Z_algorithm(S)
print(*res)
