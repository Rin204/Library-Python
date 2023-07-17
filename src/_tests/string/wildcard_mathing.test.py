# verification-helper: PROBLEM https://yukicoder.me/problems/no/2231
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.string.RollingHash import RollingHash
from src.string.wildcard_mathing import wildcard_matching


def solve():
    n, m = map(int, input().split())
    S = list(input())
    T = list(input())
    res = wildcard_matching(S, T)
    if not res:
        print(-1)
        return

    for i in range(n):
        if S[i] == "?":
            S[i] = "a"

    rhs = RollingHash(S)
    rht = RollingHash(T)

    def calc(i, l):
        if l <= i:
            return rhs.get(0, l)
        elif l <= i + m:
            return RollingHash.CalcMod(
                RollingHash.Mul(rhs.get(0, i), rhs.pw[l - i]) + rht.get(0, l - i)
            )
        else:
            return rhs.get(i + m, l)

    def get(i, l):
        if l < i:
            return S[l]
        elif l < i + m:
            return T[l - i]
        else:
            return S[l]

    ind = res[0]
    for i in range(1, len(res)):
        l = 0
        r = n
        while r - l > 1:
            mid = (l + r) // 2
            if calc(res[i], mid) == calc(ind, mid):
                l = mid
            else:
                r = mid

        if get(res[i], l) < get(ind, l):
            ind = res[i]

    for i in range(m):
        S[i + ind] = T[i]
    print(*S, sep="")


for _ in range(int(input())):
    solve()
