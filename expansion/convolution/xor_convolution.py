def xor_convolution(A, B, MOD=-1):
    """
    MOD が偶数だと壊れる
    MOD = -1 で整数指定の場合，return の直前のところを切り捨てに
    """
    n = max(len(A), len(B))
    l = (n - 1).bit_length()
    n = 1 << l
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))

    def f(A):
        h = 1
        while h < len(A):
            for i in range(0, len(A), h * 2):
                for j in range(i, i + h):
                    x = A[j]
                    y = A[j + h]
                    if MOD != -1:
                        A[j] = (x + y) % MOD
                        A[j + h] = (x - y) % MOD
            h *= 2

    f(A)
    f(B)
    if MOD != -1:
        C = [a * b % MOD for a, b in zip(A, B)]
    else:
        C = [a * b for a, b in zip(A, B)]
    f(C)
    if MOD != -1:
        inv = pow(n, MOD - 2, MOD)
        C = [c * inv % MOD for c in C]
    else:
        C = [c / n for c in C]

    return C
