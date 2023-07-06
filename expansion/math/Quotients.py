def Quotients(n):
    """
    return [(x_i, l_i, r_i), ...]
    s.t. (n / i) == x \\forall i \\in [l, r), x_i < x_{i+1}
    """

    ret = []
    l = 1
    while l <= n:
        p = n // l
        r = n // p + 1
        ret.append((p, l, r))
        l = r
    return ret[::-1]
