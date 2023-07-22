# verification-helper: PROBLEM https://judge.yosupo.jp/problem/log_of_formal_power_series
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.polynomial.FormalPowerSeries998 import FormalPowerSeries998

FPS = FormalPowerSeries998
n = int(input())
F = FPS(map(int, input().split()))
print(*F.log())
