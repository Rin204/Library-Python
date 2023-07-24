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
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegmentTree:\n    def __init__(self, n, ope, e, init=None):\n     \
    \   self.n = n\n        self.n0 = 1 << (n - 1).bit_length()\n        self.ope\
    \ = ope\n        self.e = e\n        self.data = [e] * (2 * self.n0)\n       \
    \ if init is not None:\n            for i in range(n):\n                self.data[self.n0\
    \ + i] = init[i]\n            for i in range(self.n0 - 1, 0, -1):\n          \
    \      self.data[i] = self.ope(self.data[2 * i], self.data[2 * i + 1])\n\n   \
    \ def build(self):\n        for i in range(self.n0 - 1, 0, -1):\n            self.data[i]\
    \ = self.ope(self.data[2 * i], self.data[2 * i + 1])\n\n    def set(self, i, x):\n\
    \        i += self.n0\n        self.data[i] = x\n        while i > 1:\n      \
    \      i >>= 1\n            self.data[i] = self.ope(self.data[2 * i], self.data[2\
    \ * i + 1])\n\n    def get(self, i):\n        return self.data[i + self.n0]\n\n\
    \    def __getitem__(self, i):\n        return self.data[i + self.n0]\n\n    def\
    \ __setitem__(self, i, x):\n        self.set(i, x)\n\n    def prod(self, l, r):\n\
    \        assert 0 <= l <= r <= self.n0\n        l += self.n0\n        r += self.n0\n\
    \        lles = self.e\n        rres = self.e\n        while l < r:\n        \
    \    if l & 1:\n                lles = self.ope(lles, self.data[l])\n        \
    \        l += 1\n            if r & 1:\n                r -= 1\n             \
    \   rres = self.ope(self.data[r], rres)\n            l >>= 1\n            r >>=\
    \ 1\n        return self.ope(lles, rres)\n\n    def max_right(self, l, f):\n \
    \       if l == self.n:\n            return self.n\n        l += self.n0\n   \
    \     sm = self.e\n        while 1:\n            while l % 2 == 0:\n         \
    \       l >>= 1\n            if not f(self.ope(sm, self.data[l])):\n         \
    \       while l < self.n0:\n                    l <<= 1\n                    if\
    \ f(self.ope(sm, self.data[l])):\n                        sm = self.ope(sm, self.data[l])\n\
    \                        l += 1\n                return l - self.n0\n        \
    \    sm = self.ope(sm, self.data[l])\n            l += 1\n            if l & -l\
    \ == l:\n                break\n        return self.n\n\n    def min_left(self,\
    \ r, f):\n        if r == 0:\n            return 0\n        r += self.n0\n   \
    \     sm = self.e\n        while 1:\n            r -= 1\n            while r >\
    \ 1 and r % 2:\n                r >>= 1\n            if not f(self.ope(self.data[r],\
    \ sm)):\n                while r < self.n0:\n                    r = 2 * r + 1\n\
    \                    if f(self.ope(self.data[r], sm)):\n                     \
    \   sm = self.ope(self.data[r], sm)\n                        r -= 1\n        \
    \        return r + 1 - self.n0\n            sm = self.ope(self.data[r], sm)\n\
    \            if r & -r == r:\n                break\n        return 0\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/SegmentTree.py
  requiredBy: []
  timestamp: '2023-06-13 02:09:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/SegmentTree.py
layout: document
title: SegmentTree
---

# 概要
主に 1 点更新と区間に対する演算に高速に答えるためのデータ構造です．

## 使い方
- \_\_init\_\_(n, ope, e, init=None) := 長さ $n$ の配列 A を作成します．`ope` が指定する演算で，`e` が単位元です．`init=None`に長さ$n$の配列を指定した場合はそれが初期値に，そうでない場合は `e` が初期値になります．
- build() := セグメント木の各値を全て再計算します．（あまり用途はないですが，O(N) 個所を直接変更した後まとめて計算したい場合等）
- set(i, x) := i 番目の値を x に変更します．
- get(i) := A[i] の値を求めます．
- \_\_getitem\_\_(i) := `get(i)` と同じ
- \_\_setitem\_\_(i) := `set(i, x)` と同じ
- prod(l, r) := 区間 $[l, r)$ の演算結果を返します．
- max_right(self, l, f) := 関数 f を与えて segtree 上で二分探索をします．ac-library にあるものと同じ仕様です．
- max_left(self, r, f) := 関数 f を与えて segtree 上で二分探索をします．ac-library にあるものと同じ仕様です．
