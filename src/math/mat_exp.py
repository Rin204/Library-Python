def mat_exp(A, B, n, MOD=-1):
    le = len(A)
    while n > 0:
        if n & 1:
            C = [0] * le
            for i in range(le):
                for j in range(le):
                    C[i] += A[i][j] * B[j]
                    if MOD != -1:
                        C[i] %= MOD
            B = C
        C = [[0] * le for _ in range(le)]
        for i in range(le):
            for k in range(le):
                for j in range(le):
                    C[i][j] += A[i][k] * A[k][j]
                    if MOD != -1:
                        C[i][j] %= MOD
        A = C
        n >>= 1

    return B
