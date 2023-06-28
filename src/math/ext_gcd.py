def ext_gcd(a, b):
    """
    return (x, y, gcd(a, b)) s.t. ax + by = gcd(a, b)
    """
    if b == 0:
        return 1, 0, a
    else:
        y, x, g = ext_gcd(b, a % b)
        return x, y - (a // b) * x, g
