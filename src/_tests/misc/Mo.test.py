# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.misc.Mo import Mo
from src.data_structure.BIT import BIT
import sys

input = sys.stdin.readline

n, Q = map(int, input().split())
A = list(map(int, input().split()))
dic = {a: i for i, a in enumerate(sorted(set(A)))}
A = [dic[a] for a in A]

mo = Mo(n, Q)
for _ in range(Q):
    l, r = map(int, input().split())
    mo.insert(l, r)

n = len(dic)
bit = BIT(n)
ans = [0] * Q
inv = 0


def add_left(i):
    global inv
    a = A[i]
    inv += bit.sum(a)
    bit.add(a, 1)


def add_right(i):
    global inv
    a = A[i]
    inv += bit.sum(a + 1, n)
    bit.add(a, 1)


def delete_left(i):
    global inv
    a = A[i]
    inv -= bit.sum(a)
    bit.add(a, -1)


def delete_right(i):
    global inv
    a = A[i]
    inv -= bit.sum(a + 1, n)
    bit.add(a, -1)


def rem(i):
    ans[i] = inv


mo.run(add_left, add_right, delete_left, delete_right, rem)
print(*ans, sep="\n")
