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
  code: "class SWAG:\n    def __init__(self, ope, e):\n        self.L = []\n     \
    \   self.R = []\n        self.Lcum = [e]\n        self.Rall = e\n        self.ope\
    \ = ope\n        self.e = e\n\n    def push(self, x):\n        self.R.append(x)\n\
    \        self.Rall = self.ope(self.Rall, x)\n\n    def pop(self):\n        if\
    \ not self.L:\n            while self.R:\n                self.L.append(self.R.pop())\n\
    \                self.Lcum.append(self.ope(self.L[-1], self.Lcum[-1]))\n     \
    \       self.Rall = self.e\n        self.L.pop()\n        self.Lcum.pop()\n\n\
    \    def prod(self):\n        return self.ope(self.Lcum[-1], self.Rall)\n\n  \
    \  def size(self):\n        return len(self.L) + len(self.R)\n\n    def __len__(self):\n\
    \        return self.size()\n\n    def clear(self):\n        self.L = []\n   \
    \     self.R = []\n        self.Lcum = [self.e]\n        self.Rall = self.e\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/data_structure/SWAG.py
  requiredBy: []
  timestamp: '2023-06-21 23:36:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/data_structure/SWAG.py
layout: document
title: SWAG
---

# 概要
deque に対して要素の追加 / 削除 / 現在の列に対する演算結果取得 を処理します．

演算については
- $f(a, f(b, c)) = f(f(a, b), c)$
- 単位元が存在する

ものを想定しています．（本当は単位元はいらないはずなんですが，実装の都合上要求しているので，ない場合は適当に取りえない値を設定して演算の中で if 文を入れてください）


## 使い方
- \_\_init\_\_(ope, e) := 扱う演算を定義します
- push(x) := deque の末尾に x を追加します．
- pop(x) := deque の先頭の要素を削除します．
- prod() := 現在の deque 列に対する演算結果を返します
- size() := deque 列の長さを返します．
- \_\_len\_\_ := 上記同様
- clear() := deque を空にします．
