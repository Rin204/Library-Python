# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def CartesianTree(A):
    n = len(A)
    P = [-1] * n
    B = [-1] * n
    p = -1

    for i, a in enumerate(A):
        while p >= 0 and a < A[B[p]]:
            j = B[p]
            p -= 1
            if p >= 0 and a < A[B[p]]:
                P[j] = B[p]
            else:
                P[j] = i

        p += 1
        B[p] = i

    for i in range(p, 0, -1):
        P[B[i]] = B[i - 1]

    i = B[0]
    P[i] = i
    return P


n = int(input())
A = list(map(int, input().split()))
print(*CartesianTree(A))
