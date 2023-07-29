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
  code: "from collections import deque\n\n\nclass AhoCorasick:\n    def __init__(self,\
    \ words=None):\n        if words is None:\n            self.words = []\n     \
    \   else:\n            self.words = words\n\n    def register(self, word):\n \
    \       self.words.append(word)\n\n    def build(self):\n        self.children\
    \ = [{}]\n        self.match = [[]]\n\n        for i, word in enumerate(self.words):\n\
    \            self._register(i, word)\n\n        self.failure = [0] * len(self.children)\n\
    \        self._create_failure()\n\n    def _register(self, i, word):\n       \
    \ k = 0\n        for s in word:\n            if s in self.children[k]:\n     \
    \           k = self.children[k][s]\n            else:\n                le = len(self.children)\n\
    \                self.children[k][s] = le\n                self.children.append({})\n\
    \                self.match.append([])\n                k = le\n\n        self.match[k].append(i)\n\
    \n    def _create_failure(self):\n        queue = deque(self.children[0].values())\n\
    \        while queue:\n            k = queue.popleft()\n            b = self.failure[k]\n\
    \            for s, j in self.children[k].items():\n                self.failure[j]\
    \ = self._next(b, s)\n                self.match[j] += self.match[self.failure[j]]\n\
    \                queue.append(j)\n\n    def _next(self, k, s):\n        while\
    \ 1:\n            if s in self.children[k]:\n                return self.children[k][s]\n\
    \            elif k == 0:\n                return 0\n\n            k = self.failure[k]\n\
    \n    def search(self, text):\n        k = 0\n        le = len(text)\n       \
    \ matched = [[] for _ in range(le)]\n        for i, s in enumerate(text):\n  \
    \          k = self._next(k, s)\n            for m in self.match[k]:\n       \
    \         matched[i - len(self.words[m]) + 1].append(m)\n\n        return matched\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/string/AhoCorasick.py
  requiredBy: []
  timestamp: '2023-07-09 18:05:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/string/AhoCorasick.py
layout: document
title: AhoCorasick
---

# 概要
AhoCorasick です．

## 使い方
- \_\_init\_\_(words=None) := words を指定すると，それをあらかじめ登録してくれます．
- register(word) := word を登録します
- build() := 与えられた word を用いて王地区します．
- search(text) := 以下の2次元配列の形式で登録した word と match する箇所を返します．
  - matched[i] := $[j_1, j_2, \ldots]$ ($j_1, j_2, \ldots$ はtext$[i:i+|word_j|] = words[j]$ であるもの全て)
