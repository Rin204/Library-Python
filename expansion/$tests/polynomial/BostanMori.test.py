# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class NTT998:
    # fmt: off
    rate2=(0, 911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 867605899, 0)
    irate2=(0, 86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 103369235, 0)
    rate3=(0, 372528824, 337190230, 454590761, 816400692, 578227951, 180142363, 83780245, 6597683, 70046822, 623238099, 183021267, 402682409, 631680428, 344509872, 689220186, 365017329, 774342554, 729444058, 102986190, 128751033, 395565204, 0)
    irate3=(0, 509520358, 929031873, 170256584, 839780419, 282974284, 395914482, 444904435, 72135471, 638914820, 66769500, 771127074, 985925487, 262319669, 262341272, 625870173, 768022760, 859816005, 914661783, 430819711, 272774365, 530924681, 0)
    # fmt: on

    def butterfly(A):
        n = len(A)
        h = (n - 1).bit_length()
        le = 0
        while le < h:
            if h - le == 1:
                p = 1 << (h - le - 1)
                rot = 1
                for s in range(1 << le):
                    offset = s << (h - le)
                    for i in range(p):
                        l = A[i + offset]
                        r = A[i + offset + p] * rot
                        A[i + offset] = (l + r) % 998244353
                        A[i + offset + p] = (l - r) % 998244353
                    rot *= NTT998.rate2[(~s & -~s).bit_length()]
                    rot %= 998244353
                le += 1
            else:
                p = 1 << (h - le - 2)
                rot = 1
                for s in range(1 << le):
                    rot2 = rot * rot % 998244353
                    rot3 = rot2 * rot % 998244353
                    offset = s << (h - le)
                    for i in range(p):
                        a0 = A[i + offset]
                        a1 = A[i + offset + p] * rot
                        a2 = A[i + offset + p * 2] * rot2
                        a3 = A[i + offset + p * 3] * rot3
                        a1na3imag = (a1 - a3) % 998244353 * 911660635
                        A[i + offset] = (a0 + a2 + a1 + a3) % 998244353
                        A[i + offset + p] = (a0 + a2 - a1 - a3) % 998244353
                        A[i + offset + p * 2] = (a0 - a2 + a1na3imag) % 998244353
                        A[i + offset + p * 3] = (a0 - a2 - a1na3imag) % 998244353
                    rot *= NTT998.rate3[(~s & -~s).bit_length()]
                    rot %= 998244353
                le += 2

    def butterfly_inv(A):
        n = len(A)
        h = (n - 1).bit_length()
        le = h
        while le:
            if le == 1:
                p = 1 << (h - le)
                irot = 1
                for s in range(1 << (le - 1)):
                    offset = s << (h - le + 1)
                    for i in range(p):
                        l = A[i + offset]
                        r = A[i + offset + p]
                        A[i + offset] = (l + r) % 998244353
                        A[i + offset + p] = (l - r) * irot % 998244353
                    irot *= NTT998.irate2[(~s & -~s).bit_length()]
                    irot %= 998244353
                le -= 1
            else:
                p = 1 << (h - le)
                irot = 1
                for s in range(1 << (le - 2)):
                    irot2 = irot * irot % 998244353
                    irot3 = irot2 * irot % 998244353
                    offset = s << (h - le + 2)
                    for i in range(p):
                        a0 = A[i + offset]
                        a1 = A[i + offset + p]
                        a2 = A[i + offset + p * 2]
                        a3 = A[i + offset + p * 3]
                        a2na3iimag = (a2 - a3) * 86583718 % 998244353
                        A[i + offset] = (a0 + a1 + a2 + a3) % 998244353
                        A[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % 998244353
                        A[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % 998244353
                        A[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % 998244353
                    irot *= NTT998.irate3[(~s & -~s).bit_length()]
                    irot %= 998244353
                le -= 2

    def multiply(A, B):
        n = len(A)
        m = len(B)
        if min(n, m) <= 60:
            C = [0] * (n + m - 1)
            for i in range(n):
                if i % 8 == 0:
                    for j in range(m):
                        C[i + j] += A[i] * B[j]
                        C[i + j] %= 998244353
                else:
                    for j in range(m):
                        C[i + j] += A[i] * B[j]
            return [c % 998244353 for c in C]
        A = A[:]
        B = B[:]
        z = 1 << (n + m - 2).bit_length()
        A += [0] * (z - n)
        B += [0] * (z - m)
        NTT998.butterfly(A)
        NTT998.butterfly(B)
        for i in range(z):
            A[i] *= B[i]
            A[i] %= 998244353
        NTT998.butterfly_inv(A)
        A = A[: n + m - 1]
        iz = pow(z, 998244353 - 2, 998244353)
        return [a * iz % 998244353 for a in A]


def modinv(a, MOD):
    b = MOD
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u

    if a != 1:
        return -1

    if u != 0:
        u += MOD

    return u


def BostanMori998(P, Q, n):
    le = max(len(P), len(Q))
    le = 1 << (le - 1).bit_length()
    P.extend([0] * (le - len(P)))
    Q.extend([0] * (le - len(Q)))
    while n > 0:
        P.extend([0] * le)
        Q.extend([0] * le)
        R = [x * ((1, -1)[i & 1]) for i, x in enumerate(Q)]
        NTT998.butterfly(P)
        NTT998.butterfly(Q)
        NTT998.butterfly(R)

        P = [p * r % 998244353 for p, r in zip(P, R)]
        NTT998.butterfly_inv(P)
        P = P[n % 2 :: 2]

        Q = [q * r % 998244353 for q, r in zip(Q, R)]
        NTT998.butterfly_inv(Q)
        Q = Q[::2]

        n >>= 1
    return P[0] * modinv(Q[0], 998244353) % 998244353


d, k = map(int, input().split())
A = list(map(int, input().split()))
C = [1] + [-c for c in map(int, input().split())]
P = NTT998.multiply(A, C)
P = P[:d]
ans = BostanMori998(P, C, k)
print(ans)
