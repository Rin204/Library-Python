---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: src/misc/popcount.py
    title: src/misc/popcount.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/misc/Bitset.test.py
    title: src/$tests/misc/Bitset.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from src.misc.popcount import popcount64\n\n\nclass Bitset:\n    def __init__(self,\
    \ n: int) -> None:\n        self.n = n\n        self.m = (n + 62) // 63\n    \
    \    self.A = [0] * self.m\n\n    def __len__(self) -> int:\n        return self.n\n\
    \n    @property\n    def size(self) -> int:\n        return self.n\n\n    def\
    \ __str__(self) -> str:\n        S = []\n        for a in self.A:\n          \
    \  S.append(bin(a)[2:].zfill(63)[::-1])\n        S = \"\".join(S)\n        return\
    \ S[: self.n][::-1]\n\n    def __getitem__(self, ind: int) -> int:\n        i\
    \ = ind // 63\n        j = ind - i * 63\n        return self.A[i] >> j & 1\n\n\
    \    def __setitem__(self, ind: int, k: int) -> None:\n        i = ind // 63\n\
    \        j = ind - i * 63\n        if (self.A[i] >> j & 1) != k:\n           \
    \ self.A[i] ^= 1 << j\n        else:\n            pass\n\n    def rev(self, ind:\
    \ int) -> None:\n        i = ind // 63\n        j = ind - i * 63\n        self.A[i]\
    \ ^= 1 << j\n\n    def count(self) -> int:\n        ret = 0\n        for a in\
    \ self.A:\n            ret += popcount64(a)\n        return ret\n\n    def __sum__(self)\
    \ -> int:\n        return self.count()\n\n    def resize(self, n: int) -> None:\n\
    \        m = (n + 62) // 63\n        if m > self.m:\n            self.A += [0]\
    \ * (m - self.m)\n        else:\n            self.A = self.A[:m]\n           \
    \ j = n % 63\n            if j != 0:\n                self.A[-1] &= (1 << j) -\
    \ 1\n            else:\n                pass\n        self.n = n\n        self.m\
    \ = m\n\n    def __and__(self, other: \"Bitset\") -> \"Bitset\":\n        if self.n\
    \ < other.n:\n            n = self.n\n        else:\n            n = other.n\n\
    \n        ret = Bitset(n)\n        for i, (a, b) in enumerate(zip(self.A, other.A)):\n\
    \            ret.A[i] = a & b\n\n        return ret\n\n    def __iand__(self,\
    \ other: \"Bitset\") -> \"Bitset\":\n        if self.m < other.m:\n          \
    \  m = self.m\n        else:\n            m = other.m\n        for i in range(m):\n\
    \            self.A[i] &= other.A[i]\n        for i in range(m, self.m):\n   \
    \         self.A[i] = 0\n        return self\n\n    def __or__(self, other: \"\
    Bitset\") -> \"Bitset\":\n        if self.n > other.n:\n            n = self.n\n\
    \        else:\n            n = other.n\n\n        ret = Bitset(n)\n        for\
    \ i in range(ret.m):\n            if i < self.m and i < other.m:\n           \
    \     ret.A[i] = self.A[i] | other.A[i]\n            elif i < self.m:\n      \
    \          ret.A[i] = self.A[i]\n            else:\n                ret.A[i] =\
    \ other.A[i]\n\n        return ret\n\n    def __ior__(self, other: \"Bitset\"\
    ) -> \"Bitset\":\n        if self.m < other.m:\n            m = self.m\n     \
    \   else:\n            m = other.m\n        for i in range(m):\n            self.A[i]\
    \ |= other.A[i]\n        if self.n < other.n:\n            x = self.n % 63\n \
    \           if x != 0:\n                mask = (1 << x) - 1\n                self.A[-1]\
    \ &= mask\n        else:\n            pass\n        return self\n\n    def __xor__(self,\
    \ other: \"Bitset\") -> \"Bitset\":\n        if self.n > other.n:\n          \
    \  n = self.n\n        else:\n            n = other.n\n\n        ret = Bitset(n)\n\
    \        for i in range(ret.m):\n            if i < self.m and i < other.m:\n\
    \                ret.A[i] = self.A[i] ^ other.A[i]\n            elif i < self.m:\n\
    \                ret.A[i] = self.A[i]\n            else:\n                ret.A[i]\
    \ = other.A[i]\n\n        return ret\n\n    def __ixor__(self, other: \"Bitset\"\
    ) -> \"Bitset\":\n        if self.m < other.m:\n            m = self.m\n     \
    \   else:\n            m = other.m\n        for i in range(m):\n            self.A[i]\
    \ ^= other.A[i]\n        if self.n < other.n:\n            x = self.n % 63\n \
    \           if x != 0:\n                mask = (1 << x) - 1\n                self.A[-1]\
    \ &= mask\n        else:\n            pass\n        return self\n\n    def and_count(self,\
    \ other: \"Bitset\") -> int:\n        ret = 0\n        for a, b in zip(self.A,\
    \ other.A):\n            ret += popcount64(a & b)\n        return ret\n\n    def\
    \ or_count(self, other: \"Bitset\") -> int:\n        ret = 0\n        if self.m\
    \ < other.m:\n            m = self.m\n        else:\n            m = other.m\n\
    \        for a, b in zip(self.A[:m], other.A[:m]):\n            ret += popcount64(a\
    \ | b)\n\n        for a in self.A[m:]:\n            ret += popcount64(a)\n\n \
    \       for a in other.A[m:]:\n            ret += popcount64(a)\n\n        return\
    \ ret\n\n    def xor_count(self, other: \"Bitset\") -> int:\n        ret = 0\n\
    \        if self.m < other.m:\n            m = self.m\n        else:\n       \
    \     m = other.m\n        for a, b in zip(self.A[:m], other.A[:m]):\n       \
    \     ret += popcount64(a ^ b)\n\n        for a in self.A[m:]:\n            ret\
    \ += popcount64(a)\n\n        for a in other.A[m:]:\n            ret += popcount64(a)\n\
    \n        return ret\n\n    def __rshift__(self, k: int) -> \"Bitset\":\n    \
    \    ret = Bitset(self.n)\n        x = k // 63\n        for i in range(x, self.m):\n\
    \            ret.A[i - x] = self.A[i]\n        k -= x * 63\n        if k != 0:\n\
    \            mask = (1 << k) - 1\n            rk = 63 - k\n            for i,\
    \ a in enumerate(ret.A):\n                if i != 0:\n                    ret.A[i\
    \ - 1] |= (a & mask) << (rk)\n                ret.A[i] = a >> k\n        else:\n\
    \            pass\n        return ret\n\n    def __irshift__(self, k: int) ->\
    \ \"Bitset\":\n        x = k // 63\n        for i in range(x, self.m):\n     \
    \       self.A[i - x] = self.A[i]\n        for i in range(self.m - x, self.m):\n\
    \            self.A[i] = 0\n        k -= x * 63\n        if k != 0:\n        \
    \    mask = (1 << k) - 1\n            rk = 63 - k\n            for i, a in enumerate(self.A):\n\
    \                if i != 0:\n                    self.A[i - 1] |= (a & mask) <<\
    \ (rk)\n                self.A[i] = a >> k\n        else:\n            pass\n\
    \        return self\n\n    def __lshift__(self, k: int) -> \"Bitset\":\n    \
    \    ret = Bitset(self.n)\n        x = k // 63\n        for i in range(x, self.m):\n\
    \            ret.A[i] = self.A[i - x]\n        k -= x * 63\n        if k != 0:\n\
    \            rk = 63 - k\n            mask = (1 << rk) - 1\n            for i\
    \ in range(self.m - 1, -1, -1):\n                ret.A[i] &= mask\n          \
    \      ret.A[i] <<= k\n                if i != 0:\n                    ret.A[i]\
    \ |= ret.A[i - 1] >> rk\n        else:\n            pass\n        return ret\n\
    \n    def __ilshift__(self, k: int) -> \"Bitset\":\n        x = k // 63\n    \
    \    for i in range(self.m - 1, x - 1, -1):\n            self.A[i] = self.A[i\
    \ - x]\n        for i in range(x - 1, -1, -1):\n            self.A[i] = 0\n  \
    \      k -= x * 63\n        if k != 0:\n            rk = 63 - k\n            mask\
    \ = (1 << rk) - 1\n            for i in range(self.m - 1, -1, -1):\n         \
    \       self.A[i] &= mask\n                self.A[i] <<= k\n                if\
    \ i != 0:\n                    self.A[i] |= self.A[i - 1] >> rk\n        else:\n\
    \            pass\n        return self\n"
  dependsOn:
  - src/misc/popcount.py
  isVerificationFile: false
  path: src/misc/Bitset.py
  requiredBy: []
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/misc/Bitset.test.py
documentation_of: src/misc/Bitset.py
layout: document
redirect_from:
- /library/src/misc/Bitset.py
- /library/src/misc/Bitset.py.html
title: src/misc/Bitset.py
---
