# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def arg_sort(xy):
    def _area(p):
        if p[0] == 0 and p[1] == 0:
            return 2
        elif p[1] < 0:
            if p[0] < 0:
                return 0
            else:
                return 1
        else:
            if p[0] >= 0:
                return 3
            else:
                return 4

    def merge_sort(xy):
        if len(xy) <= 1:
            return xy
        L = xy[: len(xy) // 2]
        R = xy[len(xy) // 2 :]
        L = merge_sort(L)
        R = merge_sort(R)
        res = []
        lp = 0
        rp = 0
        while lp < len(L) and rp < len(R):
            if _area(L[lp]) < _area(R[rp]):
                res.append(L[lp])
                lp += 1
            elif _area(L[lp]) > _area(R[rp]):
                res.append(R[rp])
                rp += 1
            else:
                if L[lp][1] * R[rp][0] < L[lp][0] * R[rp][1]:
                    res.append(L[lp])
                    lp += 1
                else:
                    res.append(R[rp])
                    rp += 1
        res += L[lp:] + R[rp:]
        return res

    return merge_sort(xy)


n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy = arg_sort(xy)
for x, y in xy:
    print(x, y)
