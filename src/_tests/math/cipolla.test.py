# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.cipolla import cipolla

for _ in range(int(input())):
    y, p = map(int, input().split())
    print(cipolla(y, p))
