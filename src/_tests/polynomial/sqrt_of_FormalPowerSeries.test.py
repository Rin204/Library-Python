# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.polynomial.FormalPowerSeries998 import FormalPowerSeries998

FPS = FormalPowerSeries998
n = int(input())
F = FPS(map(int, input().split()))
F = F.sqrt()
if F:
    print(*F)
else:
    print(-1)
