def Z_algorithm(S):
    le = len(S)
    Z = [0] * le
    Z[0] = le
    i = 1
    j = 0
    while i < le:
        while i + j < le and S[j] == S[i + j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue

        k = 1
        while i + k < le and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z
