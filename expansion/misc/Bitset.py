def popcount32(x):
    x = x - ((x >> 1) & 0x55555555)
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
    x = (x + (x >> 4)) & 0x0F0F0F0F
    x += x >> 8
    x += x >> 16
    return x & 0x0000003F


def popcount64(x):
    x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x & 0x0F0F0F0F0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F0F0F0F0F)
    x = (x & 0x00FF00FF00FF00FF) + ((x >> 8) & 0x00FF00FF00FF00FF)
    x = (x & 0x0000FFFF0000FFFF) + ((x >> 16) & 0x0000FFFF0000FFFF)
    x = (x & 0x00000000FFFFFFFF) + ((x >> 32) & 0x00000000FFFFFFFF)
    return x


class Bitset:
    def __init__(self, n: int) -> None:
        self.n = n
        self.m = (n + 62) // 63
        self.A = [0] * self.m

    def __len__(self) -> int:
        return self.n

    @property
    def size(self) -> int:
        return self.n

    def __str__(self) -> str:
        S = []
        for a in self.A:
            S.append(bin(a)[2:].zfill(63)[::-1])
        S = "".join(S)
        return S[: self.n][::-1]

    def __getitem__(self, ind: int) -> int:
        i = ind // 63
        j = ind - i * 63
        return self.A[i] >> j & 1

    def __setitem__(self, ind: int, k: int) -> None:
        i = ind // 63
        j = ind - i * 63
        if (self.A[i] >> j & 1) != k:
            self.A[i] ^= 1 << j
        else:
            pass

    def rev(self, ind: int) -> None:
        i = ind // 63
        j = ind - i * 63
        self.A[i] ^= 1 << j

    def count(self) -> int:
        ret = 0
        for a in self.A:
            ret += popcount64(a)
        return ret

    def __sum__(self) -> int:
        return self.count()

    def resize(self, n: int) -> None:
        m = (n + 62) // 63
        if m > self.m:
            self.A += [0] * (m - self.m)
        else:
            self.A = self.A[:m]
            j = n % 63
            if j != 0:
                self.A[-1] &= (1 << j) - 1
            else:
                pass
        self.n = n
        self.m = m

    def __and__(self, other: "Bitset") -> "Bitset":
        if self.n < other.n:
            n = self.n
        else:
            n = other.n

        ret = Bitset(n)
        for i, (a, b) in enumerate(zip(self.A, other.A)):
            ret.A[i] = a & b

        return ret

    def __iand__(self, other: "Bitset") -> "Bitset":
        if self.m < other.m:
            m = self.m
        else:
            m = other.m
        for i in range(m):
            self.A[i] &= other.A[i]
        for i in range(m, self.m):
            self.A[i] = 0
        return self

    def __or__(self, other: "Bitset") -> "Bitset":
        if self.n > other.n:
            n = self.n
        else:
            n = other.n

        ret = Bitset(n)
        for i in range(ret.m):
            if i < self.m and i < other.m:
                ret.A[i] = self.A[i] | other.A[i]
            elif i < self.m:
                ret.A[i] = self.A[i]
            else:
                ret.A[i] = other.A[i]

        return ret

    def __ior__(self, other: "Bitset") -> "Bitset":
        if self.m < other.m:
            m = self.m
        else:
            m = other.m
        for i in range(m):
            self.A[i] |= other.A[i]
        if self.n < other.n:
            x = self.n % 63
            if x != 0:
                mask = (1 << x) - 1
                self.A[-1] &= mask
        else:
            pass
        return self

    def __xor__(self, other: "Bitset") -> "Bitset":
        if self.n > other.n:
            n = self.n
        else:
            n = other.n

        ret = Bitset(n)
        for i in range(ret.m):
            if i < self.m and i < other.m:
                ret.A[i] = self.A[i] ^ other.A[i]
            elif i < self.m:
                ret.A[i] = self.A[i]
            else:
                ret.A[i] = other.A[i]

        return ret

    def __ixor__(self, other: "Bitset") -> "Bitset":
        if self.m < other.m:
            m = self.m
        else:
            m = other.m
        for i in range(m):
            self.A[i] ^= other.A[i]
        if self.n < other.n:
            x = self.n % 63
            if x != 0:
                mask = (1 << x) - 1
                self.A[-1] &= mask
        else:
            pass
        return self

    def and_count(self, other: "Bitset") -> int:
        ret = 0
        for a, b in zip(self.A, other.A):
            ret += popcount64(a & b)
        return ret

    def or_count(self, other: "Bitset") -> int:
        ret = 0
        if self.m < other.m:
            m = self.m
        else:
            m = other.m
        for a, b in zip(self.A[:m], other.A[:m]):
            ret += popcount64(a | b)

        for a in self.A[m:]:
            ret += popcount64(a)

        for a in other.A[m:]:
            ret += popcount64(a)

        return ret

    def xor_count(self, other: "Bitset") -> int:
        ret = 0
        if self.m < other.m:
            m = self.m
        else:
            m = other.m
        for a, b in zip(self.A[:m], other.A[:m]):
            ret += popcount64(a ^ b)

        for a in self.A[m:]:
            ret += popcount64(a)

        for a in other.A[m:]:
            ret += popcount64(a)

        return ret

    def __rshift__(self, k: int) -> "Bitset":
        ret = Bitset(self.n)
        x = k // 63
        for i in range(x, self.m):
            ret.A[i - x] = self.A[i]
        k -= x * 63
        if k != 0:
            mask = (1 << k) - 1
            rk = 63 - k
            for i, a in enumerate(ret.A):
                if i != 0:
                    ret.A[i - 1] |= (a & mask) << (rk)
                ret.A[i] = a >> k
        else:
            pass
        return ret

    def __irshift__(self, k: int) -> "Bitset":
        x = k // 63
        for i in range(x, self.m):
            self.A[i - x] = self.A[i]
        for i in range(self.m - x, self.m):
            self.A[i] = 0
        k -= x * 63
        if k != 0:
            mask = (1 << k) - 1
            rk = 63 - k
            for i, a in enumerate(self.A):
                if i != 0:
                    self.A[i - 1] |= (a & mask) << (rk)
                self.A[i] = a >> k
        else:
            pass
        return self

    def __lshift__(self, k: int) -> "Bitset":
        ret = Bitset(self.n)
        x = k // 63
        for i in range(x, self.m):
            ret.A[i] = self.A[i - x]
        k -= x * 63
        if k != 0:
            rk = 63 - k
            mask = (1 << rk) - 1
            for i in range(self.m - 1, -1, -1):
                ret.A[i] &= mask
                ret.A[i] <<= k
                if i != 0:
                    ret.A[i] |= ret.A[i - 1] >> rk
        else:
            pass
        return ret

    def __ilshift__(self, k: int) -> "Bitset":
        x = k // 63
        for i in range(self.m - 1, x - 1, -1):
            self.A[i] = self.A[i - x]
        for i in range(x - 1, -1, -1):
            self.A[i] = 0
        k -= x * 63
        if k != 0:
            rk = 63 - k
            mask = (1 << rk) - 1
            for i in range(self.m - 1, -1, -1):
                self.A[i] &= mask
                self.A[i] <<= k
                if i != 0:
                    self.A[i] |= self.A[i - 1] >> rk
        else:
            pass
        return self
