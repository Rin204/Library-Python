---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nimport heapq\n\n\nclass DeletableHeapq:\n    def __init__(self, lst=None, reverse=False):\n\
    \        if reverse:\n            self.pm = -1\n        else:\n            self.pm\
    \ = 1\n        if lst is None:\n            self.hq = []\n        else:\n    \
    \        self.hq = [self.pm * x for x in lst]\n\n        heapq.heapify(self.hq)\n\
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
    \            heapq.heappop(self.hq)\n\n\nclass TopKHeap:\n    def __init__(self,\
    \ K, reverse=False, A=None):\n        self.K = K\n        if not reverse:\n  \
    \          self.upp = DeletableHeapq()\n            self.low = DeletableHeapq(reverse=True)\n\
    \        else:\n            self.upp = DeletableHeapq(reverse=True)\n        \
    \    self.low = DeletableHeapq()\n\n        if A is not None:\n            for\
    \ a in A:\n                self.push(a)\n\n    def __len__(self):\n        return\
    \ len(self.upp) + len(self.low)\n\n    @property\n    def tot(self):\n       \
    \ return self.upp.tot\n\n    @property\n    def sum(self):\n        return self.upp.sum\n\
    \n    def push(self, x):\n        self.upp.push(x)\n        if len(self.upp) >\
    \ self.K:\n            self.low.push(self.upp.pop())\n\n    def remove(self, x):\n\
    \        if len(self.low) > 0 and x <= self.low[0]:\n            self.low.remove(x)\n\
    \        else:\n            self.upp.remove(x)\n            if len(self.low) >\
    \ 0:\n                self.upp.push(self.low.pop())\n\n\nimport random\n\n\nk\
    \ = random.randrange(1000, 2000)\nA = [random.randrange(10**9) for _ in range(k)]\n\
    hq = TopKHeap(k, False, A)\nQ = 1000\nfor _ in range(Q):\n    t = random.randrange(2)\n\
    \    if t == 0:\n        a = random.randrange(10**9)\n        hq.push(a)\n   \
    \     A.append(a)\n    else:\n        a = random.choice(A)\n        hq.remove(a)\n\
    \        A.remove(a)\n\n    A.sort(reverse=True)\n    assert hq.tot == sum(A[:k])\n\
    \na, b = map(int, input().split())\nprint(a + b)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/misc/TopKHeap.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/misc/TopKHeap.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/misc/TopKHeap.test.py
- /verify/expansion/$tests/misc/TopKHeap.test.py.html
title: expansion/$tests/misc/TopKHeap.test.py
---
