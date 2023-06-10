# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test


def MillerRabin(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    if n < 4759123141:
        A = [2, 7, 61]
    else:
        A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1

    for a in A:
        if a % n == 0:
            return True
        x = pow(a, d, n)
        if x != 1:
            for t in range(s):
                if x == n - 1:
                    break
                x = x * x % n
            else:
                return False
    return True


Q = int(input())
for _ in range(Q):
    n = int(input())
    if MillerRabin(n):
        print("Yes")
    else:
        print("No")
