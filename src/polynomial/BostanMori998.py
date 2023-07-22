from src.convolution.NTT998 import NTT998
from src.math.modinv import modinv


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
