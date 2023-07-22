# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_formal_power_series
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.polynomial.FormalPowerSeries998 import FormalPowerSeries998

FPS = FormalPowerSeries998
n, m = map(int, input().split())
F = FPS(map(int, input().split()))
print(*F.pow(m))
