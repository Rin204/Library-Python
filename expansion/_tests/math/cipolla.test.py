# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def cipolla(x, MOD):
    if MOD == 2:
        return x
    elif x == 0:
        return 0
    elif pow(x, (MOD - 1) // 2, MOD) != 1:
        return -1

    y = 1
    while pow((y * y - x) % MOD, (MOD - 1) // 2, MOD) == 1:
        y += 1

    base = (y * y - x) % MOD

    def multi(a0, b0, a1, b1):
        return (a0 * a1 + base * (b0 * b1 % MOD)) % MOD, (a0 * b1 + a1 * b0) % MOD

    def pow_(a, b, n):
        if n == 0:
            return 1, 0

        tmp = multi(a, b, a, b)
        ret = pow_(tmp[0], tmp[1], n >> 1)
        if n & 1:
            ret = multi(ret[0], ret[1], a, b)

        return ret

    return pow_(y, 1, (MOD + 1) // 2)[0]


for _ in range(int(input())):
    y, p = map(int, input().split())
    print(cipolla(y, p))
