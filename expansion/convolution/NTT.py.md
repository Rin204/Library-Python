---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class NTT:\n    def __init__(self, MOD=998244353):\n        self.MOD = MOD\n\
    \        self.make_info(MOD)\n\n    def make_info(self, MOD):\n        g = self.primitive_root(MOD)\n\
    \        m = MOD - 1\n        rank2 = (m & -m).bit_length() - 1\n        root\
    \ = [0] * (rank2 + 1)\n        iroot = [0] * (rank2 + 1)\n        rate2 = [0]\
    \ * (rank2 + 1)\n        irate2 = [0] * (rank2 + 1)\n        rate3 = [0] * (rank2)\n\
    \        irate3 = [0] * (rank2)\n\n        root[rank2] = pow(g, (MOD - 1) >> rank2,\
    \ MOD)\n        iroot[rank2] = pow(root[rank2], MOD - 2, MOD)\n        for i in\
    \ range(rank2 - 1, -1, -1):\n            root[i] = root[i + 1] * root[i + 1] %\
    \ MOD\n            iroot[i] = iroot[i + 1] * iroot[i + 1] % MOD\n\n        prod\
    \ = 1\n        iprod = 1\n        for i in range(1, rank2):\n            rate2[i]\
    \ = root[i + 1] * prod % MOD\n            irate2[i] = iroot[i + 1] * iprod % MOD\n\
    \            prod = prod * iroot[i + 1] % MOD\n            iprod = iprod * root[i\
    \ + 1] % MOD\n\n        prod = 1\n        iprod = 1\n        for i in range(1,\
    \ rank2 - 1):\n            rate3[i] = root[i + 2] * prod % MOD\n            irate3[i]\
    \ = iroot[i + 2] * iprod % MOD\n            prod = prod * iroot[i + 2] % MOD\n\
    \            iprod = iprod * root[i + 2] % MOD\n\n        self.IMAG = rate2[1]\n\
    \        self.IIMAG = irate2[1]\n        self.rate2 = rate2\n        self.irate2\
    \ = irate2\n        self.rate3 = rate3\n        self.irate3 = irate3\n\n    def\
    \ primitive_root(self, MOD):\n        if MOD == 998244353:\n            return\
    \ 3\n        elif MOD == 200003:\n            return 2\n        elif MOD == 167772161:\n\
    \            return 3\n        elif MOD == 469762049:\n            return 3\n\
    \        elif MOD == 754974721:\n            return 11\n        divs = [0] * 20\n\
    \        divs[0] = 2\n        cnt = 1\n        x = (MOD - 1) // 2\n        while\
    \ x % 2 == 0:\n            x //= 2\n        i = 3\n        while i * i <= x:\n\
    \            if x % i == 0:\n                divs[cnt] = i\n                cnt\
    \ += 1\n                while x % i == 0:\n                    x //= i\n     \
    \       i += 2\n        if x > 1:\n            divs[cnt] = x\n            cnt\
    \ += 1\n        g = 2\n        while 1:\n            ok = True\n            for\
    \ i in range(cnt):\n                if pow(g, (MOD - 1) // divs[i], MOD) == 1:\n\
    \                    ok = False\n                    break\n            if ok:\n\
    \                return g\n            g += 1\n\n    def butterfly(self, A):\n\
    \        n = len(A)\n        h = (n - 1).bit_length()\n        le = 0\n      \
    \  while le < h:\n            if h - le == 1:\n                p = 1 << (h - le\
    \ - 1)\n                rot = 1\n                for s in range(1 << le):\n  \
    \                  offset = s << (h - le)\n                    for i in range(p):\n\
    \                        l = A[i + offset]\n                        r = A[i +\
    \ offset + p] * rot\n                        A[i + offset] = (l + r) % self.MOD\n\
    \                        A[i + offset + p] = (l - r) % self.MOD\n            \
    \        rot *= self.rate2[(~s & -~s).bit_length()]\n                    rot %=\
    \ self.MOD\n                le += 1\n            else:\n                p = 1\
    \ << (h - le - 2)\n                rot = 1\n                for s in range(1 <<\
    \ le):\n                    rot2 = rot * rot % self.MOD\n                    rot3\
    \ = rot2 * rot % self.MOD\n                    offset = s << (h - le)\n      \
    \              for i in range(p):\n                        a0 = A[i + offset]\n\
    \                        a1 = A[i + offset + p] * rot\n                      \
    \  a2 = A[i + offset + p * 2] * rot2\n                        a3 = A[i + offset\
    \ + p * 3] * rot3\n                        a1na3imag = (a1 - a3) % self.MOD *\
    \ self.IMAG\n                        A[i + offset] = (a0 + a2 + a1 + a3) % self.MOD\n\
    \                        A[i + offset + p] = (a0 + a2 - a1 - a3) % self.MOD\n\
    \                        A[i + offset + p * 2] = (a0 - a2 + a1na3imag) % self.MOD\n\
    \                        A[i + offset + p * 3] = (a0 - a2 - a1na3imag) % self.MOD\n\
    \                    rot *= self.rate3[(~s & -~s).bit_length()]\n            \
    \        rot %= self.MOD\n                le += 2\n\n    def butterfly_inv(self,\
    \ A):\n        n = len(A)\n        h = (n - 1).bit_length()\n        le = h\n\
    \        while le:\n            if le == 1:\n                p = 1 << (h - le)\n\
    \                irot = 1\n                for s in range(1 << (le - 1)):\n  \
    \                  offset = s << (h - le + 1)\n                    for i in range(p):\n\
    \                        l = A[i + offset]\n                        r = A[i +\
    \ offset + p]\n                        A[i + offset] = (l + r) % self.MOD\n  \
    \                      A[i + offset + p] = (l - r) * irot % self.MOD\n       \
    \             irot *= self.irate2[(~s & -~s).bit_length()]\n                 \
    \   irot %= self.MOD\n                le -= 1\n            else:\n           \
    \     p = 1 << (h - le)\n                irot = 1\n                for s in range(1\
    \ << (le - 2)):\n                    irot2 = irot * irot % self.MOD\n        \
    \            irot3 = irot2 * irot % self.MOD\n                    offset = s <<\
    \ (h - le + 2)\n                    for i in range(p):\n                     \
    \   a0 = A[i + offset]\n                        a1 = A[i + offset + p]\n     \
    \                   a2 = A[i + offset + p * 2]\n                        a3 = A[i\
    \ + offset + p * 3]\n                        a2na3iimag = (a2 - a3) * self.IIMAG\
    \ % self.MOD\n                        A[i + offset] = (a0 + a1 + a2 + a3) % self.MOD\n\
    \                        A[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % self.MOD\n\
    \                        A[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 %\
    \ self.MOD\n                        A[i + offset + p * 3] = (a0 - a1 - a2na3iimag)\
    \ * irot3 % self.MOD\n                    irot *= self.irate3[(~s & -~s).bit_length()]\n\
    \                    irot %= self.MOD\n                le -= 2\n\n    def multiply(self,\
    \ A, B):\n        n = len(A)\n        m = len(B)\n        if min(n, m) <= 60:\n\
    \            C = [0] * (n + m - 1)\n            for i in range(n):\n         \
    \       if i % 8 == 0:\n                    for j in range(m):\n             \
    \           C[i + j] += A[i] * B[j]\n                        C[i + j] %= self.MOD\n\
    \                else:\n                    for j in range(m):\n             \
    \           C[i + j] += A[i] * B[j]\n            return [c % self.MOD for c in\
    \ C]\n        A = A[:]\n        B = B[:]\n        z = 1 << (n + m - 2).bit_length()\n\
    \        A += [0] * (z - n)\n        B += [0] * (z - m)\n        self.butterfly(A)\n\
    \        self.butterfly(B)\n        for i in range(z):\n            A[i] *= B[i]\n\
    \            A[i] %= self.MOD\n        self.butterfly_inv(A)\n        A = A[:\
    \ n + m - 1]\n        iz = pow(z, self.MOD - 2, self.MOD)\n        return [a *\
    \ iz % self.MOD for a in A]\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/convolution/NTT.py
  requiredBy: []
  timestamp: '2023-07-17 17:18:40+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/convolution/NTT.py
layout: document
title: NTT
---

# 概要
畳み込みです．MOD = 998244353 の場合は[専用のもの](https://github.com/Rin204/Library-Python/blob/main/src/convolution/NTT998.py)を作成しているので，そちらを使ってください．

## 使い方

- \_\_init\_\_(self, MOD) := 畳み込みに用いる MOD を指定します．
- multiply(A, B) := A と B を畳み込んだ結果を返します．
