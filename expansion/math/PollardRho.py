from math import gcd


def MillerRabin(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    if n < 4759123141:
        A = [2, 7, 61]
    else:
        A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1

    for a in A:
        if a % n == 0:
            return True
        x = pow(a, d, n)
        if x != 1:
            for t in range(s):
                if x == n - 1:
                    break
                x = x * x % n
            else:
                return False
    return True


def pollard(n):
    # https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a

    if n % 2 == 0:
        return 2

    m = int(n**0.125) + 1
    step = 0

    while 1:
        step += 1

        def f(x):
            return (x * x + step) % n

        y = k = 0
        g = q = r = 1

        while g == 1:
            x = y
            while k < 3 * r // 4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            k = r
            r <<= 1

        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x - y), n)

        if g == n:
            continue
        if MillerRabin(g):
            return g
        elif MillerRabin(n // g):
            return n // g
        else:
            return pollard(g)


def primefact(n):
    res = []
    while n > 1 and not MillerRabin(n):
        p = pollard(n)
        while n % p == 0:
            res.append(p)
            n //= p
    if n != 1:
        res.append(n)
    return sorted(res)


def primedict(n):
    P = primefact(n)
    ret = {}
    for p in P:
        ret[p] = ret.get(p, 0) + 1
    return ret
