class NTT:
    def __init__(self, MOD=998244353):
        self.MOD = MOD
        self.make_info(MOD)

    def make_info(self, MOD):
        g = self.primitive_root(MOD)
        m = MOD - 1
        rank2 = (m & -m).bit_length() - 1
        root = [0] * (rank2 + 1)
        iroot = [0] * (rank2 + 1)
        rate2 = [0] * (rank2 + 1)
        irate2 = [0] * (rank2 + 1)
        rate3 = [0] * (rank2)
        irate3 = [0] * (rank2)

        root[rank2] = pow(g, (MOD - 1) >> rank2, MOD)
        iroot[rank2] = pow(root[rank2], MOD - 2, MOD)
        for i in range(rank2 - 1, -1, -1):
            root[i] = root[i + 1] * root[i + 1] % MOD
            iroot[i] = iroot[i + 1] * iroot[i + 1] % MOD

        prod = 1
        iprod = 1
        for i in range(1, rank2):
            rate2[i] = root[i + 1] * prod % MOD
            irate2[i] = iroot[i + 1] * iprod % MOD
            prod = prod * iroot[i + 1] % MOD
            iprod = iprod * root[i + 1] % MOD

        prod = 1
        iprod = 1
        for i in range(1, rank2 - 1):
            rate3[i] = root[i + 2] * prod % MOD
            irate3[i] = iroot[i + 2] * iprod % MOD
            prod = prod * iroot[i + 2] % MOD
            iprod = iprod * root[i + 2] % MOD

        self.IMAG = rate2[1]
        self.IIMAG = irate2[1]
        self.rate2 = rate2
        self.irate2 = irate2
        self.rate3 = rate3
        self.irate3 = irate3

    def primitive_root(self, MOD):
        if MOD == 998244353:
            return 3
        elif MOD == 200003:
            return 2
        elif MOD == 167772161:
            return 3
        elif MOD == 469762049:
            return 3
        elif MOD == 754974721:
            return 11
        divs = [0] * 20
        divs[0] = 2
        cnt = 1
        x = (MOD - 1) // 2
        while x % 2 == 0:
            x //= 2
        i = 3
        while i * i <= x:
            if x % i == 0:
                divs[cnt] = i
                cnt += 1
                while x % i == 0:
                    x //= i
            i += 2
        if x > 1:
            divs[cnt] = x
            cnt += 1
        g = 2
        while 1:
            ok = True
            for i in range(cnt):
                if pow(g, (MOD - 1) // divs[i], MOD) == 1:
                    ok = False
                    break
            if ok:
                return g
            g += 1

    def butterfly(self, A):
        n = len(A)
        h = (n - 1).bit_length()
        le = 0
        while le < h:
            if h - le == 1:
                p = 1 << (h - le - 1)
                rot = 1
                for s in range(1 << le):
                    offset = s << (h - le)
                    for i in range(p):
                        l = A[i + offset]
                        r = A[i + offset + p] * rot
                        A[i + offset] = (l + r) % self.MOD
                        A[i + offset + p] = (l - r) % self.MOD
                    rot *= self.rate2[(~s & -~s).bit_length()]
                    rot %= self.MOD
                le += 1
            else:
                p = 1 << (h - le - 2)
                rot = 1
                for s in range(1 << le):
                    rot2 = rot * rot % self.MOD
                    rot3 = rot2 * rot % self.MOD
                    offset = s << (h - le)
                    for i in range(p):
                        a0 = A[i + offset]
                        a1 = A[i + offset + p] * rot
                        a2 = A[i + offset + p * 2] * rot2
                        a3 = A[i + offset + p * 3] * rot3
                        a1na3imag = (a1 - a3) % self.MOD * self.IMAG
                        A[i + offset] = (a0 + a2 + a1 + a3) % self.MOD
                        A[i + offset + p] = (a0 + a2 - a1 - a3) % self.MOD
                        A[i + offset + p * 2] = (a0 - a2 + a1na3imag) % self.MOD
                        A[i + offset + p * 3] = (a0 - a2 - a1na3imag) % self.MOD
                    rot *= self.rate3[(~s & -~s).bit_length()]
                    rot %= self.MOD
                le += 2

    def butterfly_inv(self, A):
        n = len(A)
        h = (n - 1).bit_length()
        le = h
        while le:
            if le == 1:
                p = 1 << (h - le)
                irot = 1
                for s in range(1 << (le - 1)):
                    offset = s << (h - le + 1)
                    for i in range(p):
                        l = A[i + offset]
                        r = A[i + offset + p]
                        A[i + offset] = (l + r) % self.MOD
                        A[i + offset + p] = (l - r) * irot % self.MOD
                    irot *= self.irate2[(~s & -~s).bit_length()]
                    irot %= self.MOD
                le -= 1
            else:
                p = 1 << (h - le)
                irot = 1
                for s in range(1 << (le - 2)):
                    irot2 = irot * irot % self.MOD
                    irot3 = irot2 * irot % self.MOD
                    offset = s << (h - le + 2)
                    for i in range(p):
                        a0 = A[i + offset]
                        a1 = A[i + offset + p]
                        a2 = A[i + offset + p * 2]
                        a3 = A[i + offset + p * 3]
                        a2na3iimag = (a2 - a3) * self.IIMAG % self.MOD
                        A[i + offset] = (a0 + a1 + a2 + a3) % self.MOD
                        A[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % self.MOD
                        A[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % self.MOD
                        A[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % self.MOD
                    irot *= self.irate3[(~s & -~s).bit_length()]
                    irot %= self.MOD
                le -= 2

    def multiply(self, A, B):
        n = len(A)
        m = len(B)
        if min(n, m) <= 60:
            C = [0] * (n + m - 1)
            for i in range(n):
                if i % 8 == 0:
                    for j in range(m):
                        C[i + j] += A[i] * B[j]
                        C[i + j] %= self.MOD
                else:
                    for j in range(m):
                        C[i + j] += A[i] * B[j]
            return [c % self.MOD for c in C]
        A = A[:]
        B = B[:]
        z = 1 << (n + m - 2).bit_length()
        A += [0] * (z - n)
        B += [0] * (z - m)
        self.butterfly(A)
        self.butterfly(B)
        for i in range(z):
            A[i] *= B[i]
            A[i] %= self.MOD
        self.butterfly_inv(A)
        A = A[: n + m - 1]
        iz = pow(z, self.MOD - 2, self.MOD)
        return [a * iz % self.MOD for a in A]
