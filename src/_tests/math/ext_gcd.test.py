# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.ext_gcd import ext_gcd


a, b = map(int, input().split())
x, y, g = ext_gcd(a, b)
print(x, y)
