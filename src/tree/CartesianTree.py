def CartesianTree(A):
    n = len(A)
    P = [-1] * n
    B = [-1] * n
    p = -1

    for i, a in enumerate(A):
        while p >= 0 and a < A[B[p]]:
            j = B[p]
            p -= 1
            if p >= 0 and a < A[B[p]]:
                P[j] = B[p]
            else:
                P[j] = i

        p += 1
        B[p] = i

    for i in range(p, 0, -1):
        P[B[i]] = B[i - 1]

    i = B[0]
    P[i] = i
    return P
