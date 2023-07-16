MOD = 998244353


def mat_exp_global_mod(A, B, n):
    le = len(A)
    while n > 0:
        if n & 1:
            C = [0] * le
            for i in range(le):
                for j in range(le):
                    C[i] += A[i][j] * B[j]
                    C[i] %= MOD
            B = C
        C = [[0] * le for _ in range(le)]
        for i in range(le):
            for k in range(le):
                for j in range(le):
                    C[i][j] += A[i][k] * A[k][j]
                    C[i][j] %= MOD
        A = C
        n >>= 1

    return B
