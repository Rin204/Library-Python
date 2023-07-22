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


def berlekamp_massey(A, MOD):
    n = len(A)
    B = [MOD - 1]
    C = [MOD - 1]
    y = 1
    for j in range(1, n + 1):
        l = len(C)
        m = len(B)
        x = 0
        for i in range(l):
            x += C[i] * A[j - l + i]
            x %= MOD
        B.append(0)
        m += 1
        if x == 0:
            continue
        freq = x * modinv(y, MOD) % MOD
        if l < m:
            tmp = C[:]
            C = [0] * (m - l) + C
            for i in range(m):
                C[m - 1 - i] -= freq * B[m - 1 - i]
                C[m - 1 - i] %= MOD
            B = tmp
            y = x
        else:
            for i in range(m):
                C[l - 1 - i] -= freq * B[m - 1 - i]
                C[l - 1 - i] %= MOD

    return C[::-1][1:]
