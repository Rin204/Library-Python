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
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass BIT:\n    def __init__(self, n):\n        self.n = n\n        self.data\
    \ = [0] * (n + 1)\n        if n == 0:\n            self.n0 = 0\n        else:\n\
    \            self.n0 = 1 << (n.bit_length() - 1)\n\n    def sum_(self, i):\n \
    \       s = 0\n        while i > 0:\n            s += self.data[i]\n         \
    \   i -= i & -i\n        return s\n\n    def sum(self, l, r=-1):\n        if r\
    \ == -1:\n            return self.sum_(l)\n        else:\n            return self.sum_(r)\
    \ - self.sum_(l)\n\n    def get(self, i):\n        return self.sum(i, i + 1)\n\
    \n    def add(self, i, x):\n        i += 1\n        while i <= self.n:\n     \
    \       self.data[i] += x\n            i += i & -i\n\n    def lower_bound(self,\
    \ x):\n        if x <= 0:\n            return 0\n        i = 0\n        k = self.n0\n\
    \        while k > 0:\n            if i + k <= self.n and self.data[i + k] < x:\n\
    \                x -= self.data[i + k]\n                i += k\n            k\
    \ //= 2\n        return i + 1\n\n\nimport heapq\n\n\nclass DeletableHeapq:\n \
    \   def __init__(self, lst=None, reverse=False):\n        if reverse:\n      \
    \      self.pm = -1\n        else:\n            self.pm = 1\n        if lst is\
    \ None:\n            self.hq = []\n        else:\n            self.hq = [self.pm\
    \ * x for x in lst]\n\n        heapq.heapify(self.hq)\n        self.tot = sum(self.hq)\
    \ * self.pm\n        self.cnt = {}\n        for x in self.hq:\n            self.cnt[x]\
    \ = self.cnt.get(x, 0) + 1\n        self.length = len(self.hq)\n\n    def __bool__(self):\n\
    \        return bool(self.hq)\n\n    def __len__(self):\n        return self.length\n\
    \n    @property\n    def sum(self):\n        return self.tot\n\n    def top(self):\n\
    \        if self.hq:\n            return self.hq[0] * self.pm\n        else:\n\
    \            return None\n\n    def __getitem__(self, i):\n        # \u5148\u982D\
    \u8981\u7D20\u306B\u30A2\u30AF\u30BB\u30B9\u3057\u305F\u3044\u3068\u304D\u306E\
    \u307F\n        assert i == 0\n        return self.top()\n\n    def push(self,\
    \ x):\n        self.length += 1\n        self.cnt[x * self.pm] = self.cnt.get(x\
    \ * self.pm, 0) + 1\n        self.tot += x\n        heapq.heappush(self.hq, x\
    \ * self.pm)\n\n    def pop(self):\n        if not self.hq:\n            return\
    \ None\n        self.length -= 1\n        x = heapq.heappop(self.hq)\n       \
    \ self.cnt[x] -= 1\n        self.tot -= x * self.pm\n        self._delete()\n\
    \        return x * self.pm\n\n    def remove(self, x):\n        if self.cnt.get(x\
    \ * self.pm, 0) == 0:\n            return False\n        self.length -= 1\n  \
    \      self.cnt[x * self.pm] -= 1\n        self.tot -= x\n        self._delete()\n\
    \        return True\n\n    def _delete(self):\n        while self.hq and self.cnt.get(self.hq[0],\
    \ 0) == 0:\n            heapq.heappop(self.hq)\n\n\nimport random\n\nrandom.seed(10)\n\
    \nn = 500000\nt = 500000\nA = random.choices(range(n), k=t + 10)\ncnt = len(A)\n\
    tot = sum(A)\nif random.random() > 0.5:\n    hq = DeletableHeapq(A)\nelse:\n \
    \   hq = DeletableHeapq(A, reverse=True)\nbit = BIT(n)\nfor a in A:\n    bit.add(a,\
    \ 1)\n\nfor _ in range(t):\n    if random.random() < 0.3:\n        p = hq[0]\n\
    \        assert bit.get(p) >= 1\n        if hq.pm == 1:\n            assert bit.lower_bound(1)\
    \ - 1 == p\n        else:\n            assert bit.lower_bound(cnt) - 1 == p\n\
    \        bit.add(p, -1)\n        assert p == hq.pop()\n        cnt -= 1\n    \
    \    tot -= p\n    else:\n        p = random.randrange(n)\n        if bit.get(p)\
    \ == 0 or random.random() < 0.5:\n            bit.add(p, 1)\n            hq.push(p)\n\
    \            cnt += 1\n            tot += p\n        else:\n            bit.add(p,\
    \ -1)\n            assert hq.remove(p)\n            cnt -= 1\n            tot\
    \ -= p\n\n    assert len(hq) == cnt\n    assert hq.tot == tot, (_, hq.tot, tot)\n\
    \n\na, b = map(int, input().split())\nprint(a + b)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/misc/DeletableHeapq.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/misc/DeletableHeapq.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/misc/DeletableHeapq.test.py
- /verify/expansion/$tests/misc/DeletableHeapq.test.py.html
title: expansion/$tests/misc/DeletableHeapq.test.py
---
