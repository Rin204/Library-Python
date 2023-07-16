def or_convolution(A, B, MOD=-1):
    n = max(len(A), len(B))
    l = (n - 1).bit_length()
    n = 1 << l
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))

    def f(A):
        for i in range(l):
            for bit in range(n):
                if bit >> i & 1:
                    A[bit] += A[bit ^ (1 << i)]
                    if MOD != -1:
                        A[bit] %= MOD

    def invf(A):
        for i in range(l):
            for bit in range(n):
                if bit >> i & 1:
                    A[bit] -= A[bit ^ (1 << i)]
                    if MOD != -1:
                        A[bit] %= MOD

    f(A)
    f(B)
    if MOD != -1:
        C = [a * b % MOD for a, b in zip(A, B)]
    else:
        C = [a * b for a, b in zip(A, B)]
    invf(C)
    return C
