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
