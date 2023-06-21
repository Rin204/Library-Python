# verification-helper: PROBLEM https://yukicoder.me/problems/no/790
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


class Combination:
    def __init__(self, n, MOD=998244353):
        self.fact = [1] * (n + 1)
        self.invfact = [1] * (n + 1)
        self.MOD = MOD
        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % MOD

        self.invfact[n] = pow(self.fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            self.invfact[i] = self.invfact[i + 1] * (i + 1) % MOD

    def extend(self, n):
        le = len(self.fact)
        if n < le:
            return
        self.fact.extend([1] * (n - le + 1))
        self.invfact.extend([1] * (n - le + 1))
        for i in range(le, n + 1):
            self.fact[i] = self.fact[i - 1] * i % self.MOD

        self.invfact[n] = pow(self.fact[n], self.MOD - 2, self.MOD)
        for i in range(n - 1, le - 1, -1):
            self.invfact[i] = self.invfact[i + 1] * (i + 1) % self.MOD

    def nPk(self, n, k):
        if k < 0 or n < k:
            return 0
        if n >= len(self.fact):
            self.extend(n)
        return self.fact[n] * self.invfact[n - k] % self.MOD

    def nCk(self, n, k):
        if k < 0 or n < k:
            return 0
        if n >= len(self.fact):
            self.extend(n)
        return (self.fact[n] * self.invfact[n - k] % self.MOD) * self.invfact[k] % self.MOD

    def nHk(self, n, k):
        if n == 0 and k == 0:
            return 1
        return self.nCk(n + k - 1, k)

    def Catalan(self, n):
        return (self.nCk(2 * n, n) - self.nCk(2 * n, n - 1)) % self.MOD


n = int(input())
C = Combination(n)
print(C.Catalan(n))
