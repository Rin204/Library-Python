# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def manacher(S):
    n = len(S)

    n = 2 * n + 1
    L = [0] * n

    c = 0
    for i in range(n):
        j = 2 * c - i
        if i + L[j] < c + L[c]:
            L[i] = L[j]
        else:
            j = c + L[c] - i
            while (
                i - j >= 0
                and i + j < n
                and ((i + j) & 1 == 0 or S[(i - j) >> 1] == S[(i + j) >> 1])
            ):
                j += 1
            L[i] = j
            c = i

    return [l - 1 for l in L[1 : n - 1]]


S = input()
res = manacher(S)
print(*res)
