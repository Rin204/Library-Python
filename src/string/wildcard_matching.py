import random

from src.convolution.NTT998 import NTT998


def wildcard_matching(S, T, wild="?"):
    n = len(S)
    m = len(T)
    A = [0] * n
    B = [0] * m
    dic = {wild: 0}
    for i, s in enumerate(S):
        if s not in dic:
            dic[s] = random.randrange(998244353)
        A[i] = dic[s]
    for i, t in enumerate(T):
        if t not in dic:
            dic[t] = random.randrange(998244353)
        B[i] = dic[t]

    S1 = [0] * n
    S2 = [0] * n
    S3 = [0] * n
    for i, x in enumerate(A):
        y = int(x > 0)
        S1[i] = y
        S2[i] = y * x
        S3[i] = y * x * x % 998244353

    T1 = [0] * m
    T2 = [0] * m
    T3 = [0] * m
    for i, x in enumerate(B):
        y = int(x > 0)
        T1[m - 1 - i] = y
        T2[m - 1 - i] = y * x
        T3[m - 1 - i] = y * x * x % 998244353

    res1 = NTT998.multiply(S3, T1)
    res2 = NTT998.multiply(S2, T2)
    res3 = NTT998.multiply(S1, T3)
    res = []
    for i in range(n - m + 1):
        x = res1[i + m - 1] - 2 * res2[i + m - 1] + res3[i + m - 1]
        if x == 0:
            res.append(i)

    return res
