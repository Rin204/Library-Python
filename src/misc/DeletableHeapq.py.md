---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: src/misc/MadianHeap.py
    title: src/misc/MadianHeap.py
  - icon: ':x:'
    path: src/misc/TopKHeap.py
    title: src/misc/TopKHeap.py
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/misc/DeletableHeapq.test.py
    title: src/$tests/misc/DeletableHeapq.test.py
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
  code: "import heapq\n\n\nclass DeletableHeapq:\n    def __init__(self, lst=None,\
    \ reverse=False):\n        if reverse:\n            self.pm = -1\n        else:\n\
    \            self.pm = 1\n        if lst is None:\n            self.hq = []\n\
    \        else:\n            self.hq = [self.pm * x for x in lst]\n\n        heapq.heapify(self.hq)\n\
    \        self.tot = sum(self.hq) * self.pm\n        self.cnt = {}\n        for\
    \ x in self.hq:\n            self.cnt[x] = self.cnt.get(x, 0) + 1\n        self.length\
    \ = len(self.hq)\n\n    def __bool__(self):\n        return bool(self.hq)\n\n\
    \    def __len__(self):\n        return self.length\n\n    @property\n    def\
    \ sum(self):\n        return self.tot\n\n    def top(self):\n        if self.hq:\n\
    \            return self.hq[0] * self.pm\n        else:\n            return None\n\
    \n    def __getitem__(self, i):\n        # \u5148\u982D\u8981\u7D20\u306B\u30A2\
    \u30AF\u30BB\u30B9\u3057\u305F\u3044\u3068\u304D\u306E\u307F\n        assert i\
    \ == 0\n        return self.top()\n\n    def push(self, x):\n        self.length\
    \ += 1\n        self.cnt[x * self.pm] = self.cnt.get(x * self.pm, 0) + 1\n   \
    \     self.tot += x\n        heapq.heappush(self.hq, x * self.pm)\n\n    def pop(self):\n\
    \        if not self.hq:\n            return None\n        self.length -= 1\n\
    \        x = heapq.heappop(self.hq)\n        self.cnt[x] -= 1\n        self.tot\
    \ -= x * self.pm\n        self._delete()\n        return x * self.pm\n\n    def\
    \ remove(self, x):\n        if self.cnt.get(x * self.pm, 0) == 0:\n          \
    \  return False\n        self.length -= 1\n        self.cnt[x * self.pm] -= 1\n\
    \        self.tot -= x\n        self._delete()\n        return True\n\n    def\
    \ _delete(self):\n        while self.hq and self.cnt.get(self.hq[0], 0) == 0:\n\
    \            heapq.heappop(self.hq)\n"
  dependsOn: []
  isVerificationFile: false
  path: src/misc/DeletableHeapq.py
  requiredBy:
  - src/misc/TopKHeap.py
  - src/misc/MadianHeap.py
  timestamp: '2023-06-29 01:22:58+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/misc/DeletableHeapq.test.py
documentation_of: src/misc/DeletableHeapq.py
layout: document
redirect_from:
- /library/src/misc/DeletableHeapq.py
- /library/src/misc/DeletableHeapq.py.html
title: src/misc/DeletableHeapq.py
---
