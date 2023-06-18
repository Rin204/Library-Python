def next_permutation(P):
    n = len(P)
    for i in range(n - 2, -1, -1):
        if P[i] < P[i + 1]:
            l = i + 1
            r = n - 1
            while r > l:
                P[l], P[r] = P[r], P[l]
                l += 1
                r -= 1
            for j in range(i + 1, n):
                if P[i] < P[j]:
                    P[i], P[j] = P[j], P[i]
                    return True
    return False


def all_permutations(P):
    # 全列挙したい場合はソートしてある状態で渡す
    yield P
    while next_permutation(P):
        yield P


def prev_permutation(P):
    n = len(P)
    for i in range(n - 2, -1, -1):
        if P[i] > P[i + 1]:
            l = i + 1
            r = n - 1
            while r > l:
                P[l], P[r] = P[r], P[l]
                l += 1
                r -= 1
            for j in range(i + 1, n):
                if P[i] > P[j]:
                    P[i], P[j] = P[j], P[i]
                    return True
    return False


def rev_all_permutations(P):
    # 全列挙したい場合は逆順ソートしてある状態で渡す
    yield P
    while prev_permutation(P):
        yield P
