# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from functools import cmp_to_key


def sa_naive(S):
    n = len(S)
    sa = [i for i in range(n)]

    def cmp(l, r):
        if l == r:
            return 0
        while l < n and r < n:
            if S[l] != S[r]:
                return 1 - 2 * (S[l] < S[r])
            l += 1
            r += 1
        return 1 - 2 * (l == n)

    return sorted(sa, key=cmp_to_key(cmp))


def sa_doubling(S):
    n = len(S)
    sa = [i for i in range(n)]
    rnk = S[:]
    tmp = [0] * n
    k = 1
    while k < n:

        def cmp(x, y):
            if rnk[x] != rnk[y]:
                return 1 - 2 * (rnk[x] < rnk[y])

            rx = -1
            if x + k < n:
                rx = rnk[x + k]
            ry = -1
            if y + k < n:
                ry = rnk[y + k]
            return 1 - 2 * (rx < ry)

        sa.sort(key=cmp_to_key(cmp))
        tmp[sa[0]] = 0
        for i in range(n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (1 if cmp(sa[i - 1], sa[i]) == -1 else 0)
        tmp, rnk = rnk, tmp
        k <<= 1

    return sa


def sa_is(S, upper, NAIVE_THR=10, DOUBLING_THR=40):
    n = len(S)
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        if S[0] < S[1]:
            return [0, 1]
        else:
            return [1, 0]
    elif n <= NAIVE_THR:
        return sa_naive(S)
    elif n <= DOUBLING_THR:
        return sa_doubling(S)

    sa = [0] * n
    ls = [False] * n
    for i in range(n - 2, -1, -1):
        if S[i] == S[i + 1]:
            ls[i] = ls[i + 1]
        else:
            ls[i] = S[i] < S[i + 1]

    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)

    for i in range(n):
        if not ls[i]:
            sum_s[S[i]] += 1
        else:
            sum_l[S[i] + 1] += 1

    for i in range(upper + 1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]

    def induce(lms):
        nonlocal sa
        sa = [-1] * n
        buf = sum_s[:]
        for d in lms:
            if d == n:
                continue
            sa[buf[S[d]]] = d
            buf[S[d]] += 1

        buf = sum_l[:]
        sa[buf[S[n - 1]]] = n - 1
        buf[S[n - 1]] += 1
        for i in range(n):
            v = sa[i]
            if v >= 1 and not ls[v - 1]:
                sa[buf[S[v - 1]]] = v - 1
                buf[S[v - 1]] += 1

        buf = sum_l[:]
        for i in range(n - 1, -1, -1):
            v = sa[i]
            if v >= 1 and ls[v - 1]:
                buf[S[v - 1] + 1] -= 1
                sa[buf[S[v - 1] + 1]] = v - 1

    lms_map = [-1] * (n + 1)
    m = 0
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
            lms.append(i)

    induce(lms)

    if m > 0:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            l = sorted_lms[i - 1]
            r = sorted_lms[i]

            end_l = n
            if lms_map[l] + 1 < m:
                end_l = lms[lms_map[l] + 1]
            end_r = n
            if lms_map[r] + 1 < m:
                end_r = lms[lms_map[r] + 1]

            same = True
            if end_l - l != end_r - r:
                same = False
            else:
                while l < end_l:
                    if S[l] != S[r]:
                        break
                    l += 1
                    r += 1
                if l == n or S[l] != S[r]:
                    same = False

            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper

        rec_sa = sa_is(rec_s, rec_upper, NAIVE_THR, DOUBLING_THR)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]

        induce(sorted_lms)

    return sa


def suffix_array(S, NAIVE_THR=10, DOUBLING_THR=40):
    dic = {s: i for i, s in enumerate(sorted(set(S)))}
    return sa_is([dic[s] for s in S], len(dic), NAIVE_THR, DOUBLING_THR)


def lcp_array(S, sa):
    n = len(S)
    rnk = [0] * n
    for i, s in enumerate(sa):
        rnk[s] = i

    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue

        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n:
            if S[j + h] != S[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h

    return lcp


S = input()
sa = suffix_array(S)
print(*sa)
