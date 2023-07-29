---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass SegmentTreeBase_:\n    def ope(self, l, r):\n        return None\n\n\
    \    def e(self):\n        return None\n\n    def __init__(self, n, init=None):\n\
    \        self.n = n\n        self.n0 = 1 << (n - 1).bit_length()\n        self.data\
    \ = [self.e()] * (2 * self.n0)\n        if init is not None:\n            for\
    \ i in range(n):\n                self.data[self.n0 + i] = init[i]\n         \
    \   for i in range(self.n0 - 1, 0, -1):\n                self.data[i] = self.ope(self.data[2\
    \ * i], self.data[2 * i + 1])\n\n    def build(self):\n        for i in range(self.n0\
    \ - 1, 0, -1):\n            self.data[i] = self.ope(self.data[2 * i], self.data[2\
    \ * i + 1])\n\n    def set(self, i, x):\n        i += self.n0\n        self.data[i]\
    \ = x\n        while i > 1:\n            i >>= 1\n            self.data[i] = self.ope(self.data[2\
    \ * i], self.data[2 * i + 1])\n\n    def get(self, i):\n        return self.data[i\
    \ + self.n0]\n\n    def __getitem__(self, i):\n        return self.data[i + self.n0]\n\
    \n    def __setitem__(self, i, x):\n        self.set(i, x)\n\n    def prod(self,\
    \ l, r):\n        assert 0 <= l <= r <= self.n0\n        l += self.n0\n      \
    \  r += self.n0\n        lles = self.e()\n        rres = self.e()\n        while\
    \ l < r:\n            if l & 1:\n                lles = self.ope(lles, self.data[l])\n\
    \                l += 1\n            if r & 1:\n                r -= 1\n     \
    \           rres = self.ope(self.data[r], rres)\n            l >>= 1\n       \
    \     r >>= 1\n        return self.ope(lles, rres)\n\n    def max_right(self,\
    \ l, f):\n        if l == self.n:\n            return self.n\n        l += self.n0\n\
    \        sm = self.e()\n        while 1:\n            while l % 2 == 0:\n    \
    \            l >>= 1\n            if not f(self.ope(sm, self.data[l])):\n    \
    \            while l < self.n0:\n                    l <<= 1\n               \
    \     if f(self.ope(sm, self.data[l])):\n                        sm = self.ope(sm,\
    \ self.data[l])\n                        l += 1\n                return l - self.n0\n\
    \            sm = self.ope(sm, self.data[l])\n            l += 1\n           \
    \ if l & -l == l:\n                break\n        return self.n\n\n    def min_left(self,\
    \ r, f):\n        if r == 0:\n            return 0\n        r += self.n0\n   \
    \     sm = self.e()\n        while 1:\n            r -= 1\n            while r\
    \ > 1 and r % 2:\n                r >>= 1\n            if not f(self.ope(self.data[r],\
    \ sm)):\n                while r < self.n0:\n                    r = 2 * r + 1\n\
    \                    if f(self.ope(self.data[r], sm)):\n                     \
    \   sm = self.ope(self.data[r], sm)\n                        r -= 1\n        \
    \        return r + 1 - self.n0\n            sm = self.ope(self.data[r], sm)\n\
    \            if r & -r == r:\n                break\n        return 0\n\n\nMOD\
    \ = 998244353\n\n\nclass PointSetRangeComposite(SegmentTreeBase_):\n    def ope(self,\
    \ l, r):\n        a = l >> 30\n        b = l ^ (a << 30)\n        c = r >> 30\n\
    \        d = r ^ (c << 30)\n\n        e = (a * c) % MOD\n        f = (b * c +\
    \ d) % MOD\n\n        return (e << 30) | f\n\n    def e(self):\n        return\
    \ 1 << 30\n\n\nn, Q = map(int, input().split())\nA = [0] * n\nfor i in range(n):\n\
    \    a, b = map(int, input().split())\n    A[i] = (a << 30) | b\nseg = PointSetRangeComposite(n,\
    \ A)\nfor _ in range(Q):\n    t, p, c, d = map(int, input().split())\n    if t\
    \ == 0:\n        seg[p] = (c << 30) | d\n    else:\n        res = seg.prod(p,\
    \ c)\n        a = res >> 30\n        b = res ^ (a << 30)\n        ans = (a * d\
    \ + b) % MOD\n        print(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/segtree3.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/segtree3.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/segtree3.test.py
- /verify/expansion/$tests/data_structure/segtree3.test.py.html
title: expansion/$tests/data_structure/segtree3.test.py
---