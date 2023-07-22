# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.data_structure.SWAG import SWAG


MOD = 998244353


def ope(l, r):
    a = l >> 30
    b = l ^ (a << 30)
    c = r >> 30
    d = r ^ (c << 30)

    e = (a * c) % MOD
    f = (b * c + d) % MOD

    return (e << 30) | f


Q = int(input())
swag = SWAG(ope, 1 << 30)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        swag.push((query[1] << 30) | query[2])
    elif query[0] == 1:
        swag.pop()
    else:
        res = swag.prod()
        a = res >> 30
        b = res ^ (a << 30)
        ans = (a * query[1] + b) % MOD
        print(ans)
