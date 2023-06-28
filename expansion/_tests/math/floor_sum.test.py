# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def floor_sum(n, m, a, b):
    """
    return \\sum_{i=0}^{n-1} ((a*i+b)//m)
    """
    ret = 0
    while True:
        if a >= m:
            ret += (n - 1) * n // 2 * (a // m)
            a %= m
        if b >= m:
            ret += n * (b // m)
            b %= m
        y_max = (a * n + b) // m
        if y_max == 0:
            return ret
        x_max = y_max * m - b
        ret += (n - (x_max + a - 1) // a) * y_max
        n, m, a, b = y_max, a, m, -x_max % a


for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
