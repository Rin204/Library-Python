---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/misc/DeletableHeapq.py
    title: src/misc/DeletableHeapq.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/misc/TopKHeap.test.py
    title: src/$tests/misc/TopKHeap.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from src.misc.DeletableHeapq import DeletableHeapq\n\n\nclass TopKHeap:\n\
    \    def __init__(self, K, reverse=False, A=None):\n        self.K = K\n     \
    \   if not reverse:\n            self.upp = DeletableHeapq()\n            self.low\
    \ = DeletableHeapq(reverse=True)\n        else:\n            self.upp = DeletableHeapq(reverse=True)\n\
    \            self.low = DeletableHeapq()\n\n        if A is not None:\n      \
    \      for a in A:\n                self.push(a)\n\n    def __len__(self):\n \
    \       return len(self.upp) + len(self.low)\n\n    @property\n    def tot(self):\n\
    \        return self.upp.tot\n\n    @property\n    def sum(self):\n        return\
    \ self.upp.sum\n\n    def push(self, x):\n        self.upp.push(x)\n        if\
    \ len(self.upp) > self.K:\n            self.low.push(self.upp.pop())\n\n    def\
    \ remove(self, x):\n        if len(self.low) > 0 and x <= self.low[0]:\n     \
    \       self.low.remove(x)\n        else:\n            self.upp.remove(x)\n  \
    \          if len(self.low) > 0:\n                self.upp.push(self.low.pop())\n"
  dependsOn:
  - src/misc/DeletableHeapq.py
  isVerificationFile: false
  path: src/misc/TopKHeap.py
  requiredBy: []
  timestamp: '2023-07-16 15:47:36+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/misc/TopKHeap.test.py
documentation_of: src/misc/TopKHeap.py
layout: document
redirect_from:
- /library/src/misc/TopKHeap.py
- /library/src/misc/TopKHeap.py.html
title: src/misc/TopKHeap.py
---
