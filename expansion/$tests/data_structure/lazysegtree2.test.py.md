---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_affine_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass LazySegmentTreeBase_:\n    def ope(self, l, r):\n        return None\n\
    \n    def e(self):\n        return None\n\n    def mapping(self, f, x):\n    \
    \    return None\n\n    def composition(self, f, g):\n        return None\n\n\
    \    def id_(self):\n        return None\n\n    def __init__(self, n, init=None):\n\
    \        self.n = n\n        self.log = (n - 1).bit_length()\n        self.n0\
    \ = 1 << self.log\n        self.data = [self.e()] * (2 * self.n0)\n        self.lazy\
    \ = [self.id_()] * self.n0\n        if init is not None:\n            for i in\
    \ range(n):\n                self.data[self.n0 + i] = init[i]\n            for\
    \ i in range(self.n0 - 1, 0, -1):\n                self.data[i] = self.ope(self.data[2\
    \ * i], self.data[2 * i + 1])\n\n    def _all_apply(self, p, f):\n        self.data[p]\
    \ = self.mapping(f, self.data[p])\n        if p < self.n0:\n            self.lazy[p]\
    \ = self.composition(f, self.lazy[p])\n\n    def _push(self, p):\n        self._all_apply(2\
    \ * p, self.lazy[p])\n        self._all_apply(2 * p + 1, self.lazy[p])\n     \
    \   self.lazy[p] = self.id_()\n\n    def _update(self, p):\n        self.data[p]\
    \ = self.ope(self.data[2 * p], self.data[2 * p + 1])\n\n    def set(self, p, x):\n\
    \        p += self.n0\n        for i in range(self.log, 0, -1):\n            self._push(p\
    \ >> i)\n\n        self.data[p] = x\n        for i in range(1, self.log + 1):\n\
    \            self._update(p >> i)\n\n    def __setitem__(self, p, x):\n      \
    \  self.set(p, x)\n\n    def get(self, p):\n        p += self.n0\n        for\
    \ i in range(self.log, 0, -1):\n            self._push(p >> i)\n        return\
    \ self.data[p]\n\n    def __getitem__(self, p):\n        return self.get(p)\n\n\
    \    def prod(self, l, r):\n        assert 0 <= l <= r <= self.n0\n        l +=\
    \ self.n0\n        r += self.n0\n\n        for i in range(self.log, 0, -1):\n\
    \            if ((l >> i) << i) != l:\n                self._push(l >> i)\n  \
    \          if ((r >> i) << i) != r:\n                self._push((r - 1) >> i)\n\
    \n        lles = self.e()\n        rres = self.e()\n        while l < r:\n   \
    \         if l & 1:\n                lles = self.ope(lles, self.data[l])\n   \
    \             l += 1\n            if r & 1:\n                r -= 1\n        \
    \        rres = self.ope(self.data[r], rres)\n            l >>= 1\n          \
    \  r >>= 1\n        return self.ope(lles, rres)\n\n    def all_prod(self):\n \
    \       return self.data[1]\n\n    def _apply(self, p, f):\n        p += self.n0\n\
    \        for i in range(self.log, 0, -1):\n            self._push(p >> i)\n  \
    \      self.data[p] = self.mapping(f, self.data[p])\n        for i in range(1,\
    \ self.log + 1):\n            self._update(p >> i)\n\n    def apply(self, l, r,\
    \ f=None):\n        if f is None:\n            self._apply(l, r)\n           \
    \ return\n\n        if l == r:\n            return\n\n        l += self.n0\n \
    \       r += self.n0\n\n        for i in range(self.log, 0, -1):\n           \
    \ if ((l >> i) << i) != l:\n                self._push(l >> i)\n            if\
    \ ((r >> i) << i) != r:\n                self._push((r - 1) >> i)\n\n        l2\
    \ = l\n        r2 = r\n        while l < r:\n            if l & 1:\n         \
    \       self._all_apply(l, f)\n                l += 1\n            if r & 1:\n\
    \                r -= 1\n                self._all_apply(r, f)\n            l\
    \ >>= 1\n            r >>= 1\n\n        l = l2\n        r = r2\n\n        for\
    \ i in range(1, self.log + 1):\n            if ((l >> i) << i) != l:\n       \
    \         self._update(l >> i)\n            if ((r >> i) << i) != r:\n       \
    \         self._update((r - 1) >> i)\n\n    def max_right(self, l, f):\n     \
    \   if l == self.n:\n            return self.n\n        l += self.n0\n       \
    \ for i in range(self.log, 0, -1):\n            self._push(l >> i)\n\n       \
    \ sm = self.e()\n        while 1:\n            while l % 2 == 0:\n           \
    \     l >>= 1\n            if not f(self.ope(sm, self.data[l])):\n           \
    \     while l < self.n0:\n                    self._push(l)\n                \
    \    l <<= 1\n                    if f(self.ope(sm, self.data[l])):\n        \
    \                sm = self.ope(sm, self.data[l])\n                        l +=\
    \ 1\n                return l - self.n0\n            sm = self.ope(sm, self.data[l])\n\
    \            l += 1\n            if l & -l == l:\n                break\n    \
    \    return self.n\n\n    def min_left(self, r, f):\n        if r == 0:\n    \
    \        return 0\n        r += self.n0\n\n        for i in range(self.log, 0,\
    \ -1):\n            if ((r >> i) << i) != r:\n                self._push((r -\
    \ 1) >> i)\n\n        sm = self.e()\n        while 1:\n            r -= 1\n  \
    \          while r > 1 and r % 2:\n                r >>= 1\n            if not\
    \ f(self.ope(self.data[r], sm)):\n                while r < self.n0:\n       \
    \             self._push(r)\n                    r = 2 * r + 1\n             \
    \       if f(self.ope(self.data[r], sm)):\n                        sm = self.ope(self.data[r],\
    \ sm)\n                        r -= 1\n                return r + 1 - self.n0\n\
    \            sm = self.ope(self.data[r], sm)\n            if r & -r == r:\n  \
    \              break\n        return 0\n\n\nMOD = 998244353\n\n\nclass RangeAffineRangeSum(LazySegmentTreeBase_):\n\
    \    def ope(self, l, r):\n        a0 = l >> 30\n        a1 = l ^ (a0 << 30)\n\
    \        b0 = r >> 30\n        b1 = r ^ (b0 << 30)\n        c0 = (a0 + b0) % MOD\n\
    \        c1 = (a1 + b1) % MOD\n        return (c0 << 30) + c1\n\n    def e(self):\n\
    \        return 0\n\n    def mapping(self, f, x):\n        a0 = f >> 30\n    \
    \    a1 = f ^ (a0 << 30)\n        b0 = x >> 30\n        b1 = x ^ (b0 << 30)\n\
    \        c0 = (a0 * b0 + a1 * b1) % MOD\n        c1 = b1\n        return (c0 <<\
    \ 30) + c1\n\n    def composition(self, f, g):\n        a0 = f >> 30\n       \
    \ a1 = f ^ (a0 << 30)\n        b0 = g >> 30\n        b1 = g ^ (b0 << 30)\n   \
    \     c0 = (a0 * b0) % MOD\n        c1 = (a0 * b1 + a1) % MOD\n        return\
    \ (c0 << 30) + c1\n\n    def id_(self):\n        return 1 << 30\n\n\nn, Q = map(int,\
    \ input().split())\nA = list(map(int, input().split()))\nA = [(a << 30) + 1 for\
    \ a in A]\n\nseg = RangeAffineRangeSum(n, A)\nfor _ in range(Q):\n    query =\
    \ list(map(int, input().split()))\n    if query[0] == 0:\n        l, r, b, c =\
    \ query[1:]\n        seg.apply(l, r, (b << 30) + c)\n    else:\n        l, r =\
    \ query[1:]\n        print(seg.prod(l, r) >> 30)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/lazysegtree2.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/lazysegtree2.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/lazysegtree2.test.py
- /verify/expansion/$tests/data_structure/lazysegtree2.test.py.html
title: expansion/$tests/data_structure/lazysegtree2.test.py
---
