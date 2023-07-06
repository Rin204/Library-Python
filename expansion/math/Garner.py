def ext_gcd(a, b):
    """
    return (x, y, gcd(a, b)) s.t. ax + by = gcd(a, b)
    """
    if b == 0:
        return 1, 0, a
    else:
        y, x, g = ext_gcd(b, a % b)
        return x, y - (a // b) * x, g


def Garner(R, M):
    r = 0
    m = 1
    for ri, mi in zip(R, M):
        if ri < 0 or mi <= ri:
            ri %= mi

        if m < mi:
            m, mi = mi, m
            r, ri = ri, r

        if m % mi == 0:
            if r % mi != ri:
                return -1, -1
            continue

        im, _, g = ext_gcd(m, mi)
        if im < 0:
            im += mi

        if (ri - r) % g != 0:
            return -1, -1

        ui = mi // g
        x = ((ri - r) // g % ui) * im % ui
        r += x * m
        m *= ui

    return r, m
