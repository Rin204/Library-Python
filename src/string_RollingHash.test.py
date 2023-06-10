# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja

from src.string.RollingHash import RollingHash


S = input()
T = input()
ls = len(S)
lt = len(T)
rh1 = RollingHash(S)
rh2 = RollingHash(T)
for i in range(ls - lt + 1):
    if rh1.get(i, i + lt) == rh2.get(0, lt):
        print(i)
