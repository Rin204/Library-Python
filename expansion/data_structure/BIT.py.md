---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BIT:\n    def __init__(self, n):\n        self.n = n\n        self.data\
    \ = [0] * (n + 1)\n        if n == 0:\n            self.n0 = 0\n        else:\n\
    \            self.n0 = 1 << (n.bit_length() - 1)\n\n    def sum_(self, i):\n \
    \       s = 0\n        while i > 0:\n            s += self.data[i]\n         \
    \   i -= i & -i\n        return s\n\n    def sum(self, l, r=-1):\n        if r\
    \ == -1:\n            return self.sum_(l)\n        else:\n            return self.sum_(r)\
    \ - self.sum_(l)\n\n    def get(self, i):\n        return self.sum(i, i + 1)\n\
    \n    def add(self, i, x):\n        i += 1\n        while i <= self.n:\n     \
    \       self.data[i] += x\n            i += i & -i\n\n    def lower_bound(self,\
    \ x):\n        if x <= 0:\n            return 0\n        i = 0\n        k = self.n0\n\
    \        while k > 0:\n            if i + k <= self.n and self.data[i + k] < x:\n\
    \                x -= self.data[i + k]\n                i += k\n            k\
    \ //= 2\n        return i + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/BIT.py
  requiredBy: []
  timestamp: '2023-06-10 15:38:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/BIT.py
layout: document
title: BIT
---

# 概要
Binary Indexed Tree / Fenwick Tree です．1点加算区間和取得を高速に行います．

## 使い方
- \_\_init\_\_(n) := 長さ $N$ の配列 A を作成します．
- sum(r) := 区間 $[0, r)$ の総和を返します．
- sum(l, r) := 区間 $[l, r)$ の総和を返します．
- get(i) := A[i] の値を求めます．
- add(i, x) := A[i] に $x$ を加算します．
- lower_bound(x) := 区間 $[0, r)$ の総和が $x$ 以上となるような最小の $k$ を返します．