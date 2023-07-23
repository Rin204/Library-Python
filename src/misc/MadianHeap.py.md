---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/misc/DeletableHeapq.py
    title: src/misc/DeletableHeapq.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/misc/MedianHeap.test.py
    title: src/$tests/misc/MedianHeap.test.py
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
  code: "from src.misc.DeletableHeapq import DeletableHeapq\n\n\nclass MedianHeap:\n\
    \    def __init__(self, A=None):\n        self.upp = DeletableHeapq()\n      \
    \  self.low = DeletableHeapq(reverse=True)\n\n        if A is not None:\n    \
    \        for a in A:\n                self.push(a)\n\n    def __len__(self):\n\
    \        return len(self.upp) + len(self.low)\n\n    def push(self, x):\n    \
    \    if len(self.upp) == len(self.low) + 1:\n            self.upp.push(x)\n  \
    \          self.low.push(self.upp.pop())\n        else:\n            self.low.push(x)\n\
    \            self.upp.push(self.low.pop())\n\n    def get_med(self):\n       \
    \ \"\"\"\n        A = [1, 2, 3] -> [2, 2] \u3092\u8FD4\u3059\n        A = [1,\
    \ 2, 3, 4] -> [2, 3] \u3092\u8FD4\u3059\n        \"\"\"\n        if len(self.upp)\
    \ == len(self.low):\n            return [self.low[0], self.upp[0]]\n        else:\n\
    \            return [self.upp[0], self.upp[0]]\n\n    def remove(self, x):\n \
    \       if x <= self.low[0]:\n            self.low.remove(x)\n            if len(self.low)\
    \ + 1 < len(self.upp):\n                self.low.push(self.upp.pop())\n      \
    \  else:\n            self.upp.remove(x)\n            if len(self.upp) < len(self.low):\n\
    \                self.upp.push(self.low.pop())\n\n    def abs_sum(self):\n   \
    \     if len(self) == 0:\n            return 0\n\n        med = self.upp[0]\n\
    \        ret = med * len(self.low) - self.low.tot\n        ret += self.upp.tot\
    \ - med * len(self.upp)\n        return ret\n"
  dependsOn:
  - src/misc/DeletableHeapq.py
  isVerificationFile: false
  path: src/misc/MadianHeap.py
  requiredBy: []
  timestamp: '2023-07-16 15:47:36+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/misc/MedianHeap.test.py
documentation_of: src/misc/MadianHeap.py
layout: document
redirect_from:
- /library/src/misc/MadianHeap.py
- /library/src/misc/MadianHeap.py.html
title: src/misc/MadianHeap.py
---
