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
  code: "from collections import deque\n\n\nclass ConvexHullTrick:\n    def __init__(self):\n\
    \        self.deq = deque()\n\n    def check(f1, f2, f3):\n        return (f2[0]\
    \ - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])\n\n    def f(self,\
    \ _f, x):\n        return _f[0] * x + _f[1]\n\n    def add_line(self, a, b):\n\
    \        \"\"\"\n        add  f_i(x) = a * x + b\n        \"\"\"\n        f =\
    \ (a, b)\n        while len(self.deq) >= 2 and ConvexHullTrick.check(self.deq[-2],\
    \ self.deq[-1], f):\n            self.deq.pop()\n        self.deq.append(f)\n\n\
    \    def get(self, x):\n        \"\"\"\n        return min_i f_i(x)\n        \"\
    \"\"\n        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1],\
    \ x):\n            self.deq.popleft()\n\n        return self.f(self.deq[0], x)\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/ConvexHullTrick.py
  requiredBy: []
  timestamp: '2023-07-12 23:29:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/ConvexHullTrick.py
layout: document
title: ConvexHullTrick
---

# 概要
以下のクエリを処理します

- 1 次関数 $f(x) = ax + b$ を追加
- 追加された 1 次関数のうち ある x において最小値を取るもの（の $f(x)$ の値）を返す

ただし，
- 追加する 1 時間数の傾きが単調減少である
- 最小値クエリの x の値が単調増加である

必要があります．増加 / 減少を逆にしたい場合は適当に -1 をかけて調整してください



## 使い方
- \_\_init\_\_() := 
- add_line(a, b) := $f(x) = ax + b$ を追加します．
- get(x) := x における最小値を返します
