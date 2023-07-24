---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_inversions_query
    links:
    - https://judge.yosupo.jp/problem/static_range_inversions_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass MoBase_:\n    def add_left(self, i):\n        pass\n\n    def add_right(self,\
    \ i):\n        pass\n\n    def delete_left(self, i):\n        pass\n\n    def\
    \ delete_right(self, i):\n        pass\n\n    def rem(self, i):\n        pass\n\
    \n    def __init__(self, n, Q):\n        self.n = n\n        self.Q = Q\n    \
    \    self.width = int(max(1, n / max(1, Q * 2.0 / 3.0) ** 0.5))\n        self.L\
    \ = []\n        self.R = []\n\n    def insert(self, l, r):\n        self.L.append(l)\n\
    \        self.R.append(r)\n\n    def run(self):\n        def cmp(i):\n       \
    \     b = self.L[i] // self.width\n            res = b * self.n * 3\n        \
    \    if b % 2 == 0:\n                res += self.R[i]\n            else:\n   \
    \             res -= self.R[i]\n            return res\n\n        order = [(i,\
    \ cmp(i)) for i in range(self.Q)]\n\n        order.sort(key=lambda x: x[1])\n\
    \        nl = 0\n        nr = 0\n        for i, _ in order:\n            l = self.L[i]\n\
    \            r = self.R[i]\n            while nl > l:\n                nl -= 1\n\
    \                self.add_left(nl)\n            while nr < r:\n              \
    \  self.add_right(nr)\n                nr += 1\n            while nl < l:\n  \
    \              self.delete_left(nl)\n                nl += 1\n            while\
    \ nr > r:\n                nr -= 1\n                self.delete_right(nr)\n  \
    \          self.rem(i)\n\n\nclass BIT:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.data = [0] * (n + 1)\n        if n == 0:\n            self.n0\
    \ = 0\n        else:\n            self.n0 = 1 << (n.bit_length() - 1)\n\n    def\
    \ sum_(self, i):\n        s = 0\n        while i > 0:\n            s += self.data[i]\n\
    \            i -= i & -i\n        return s\n\n    def sum(self, l, r=-1):\n  \
    \      if r == -1:\n            return self.sum_(l)\n        else:\n         \
    \   return self.sum_(r) - self.sum_(l)\n\n    def get(self, i):\n        return\
    \ self.sum(i, i + 1)\n\n    def add(self, i, x):\n        i += 1\n        while\
    \ i <= self.n:\n            self.data[i] += x\n            i += i & -i\n\n   \
    \ def lower_bound(self, x):\n        if x <= 0:\n            return 0\n      \
    \  i = 0\n        k = self.n0\n        while k > 0:\n            if i + k <= self.n\
    \ and self.data[i + k] < x:\n                x -= self.data[i + k]\n         \
    \       i += k\n            k //= 2\n        return i + 1\n\n\nimport sys\n\n\
    input = sys.stdin.readline\n\nn, Q = map(int, input().split())\nA = list(map(int,\
    \ input().split()))\ndic = {a: i for i, a in enumerate(sorted(set(A)))}\nA = [dic[a]\
    \ for a in A]\n\n\nclass Mo(MoBase_):\n    def __init__(self, n, Q):\n       \
    \ super().__init__(n, Q)\n        self.inv = 0\n\n    def add_left(self, i):\n\
    \        a = A[i]\n        self.inv += bit.sum(a)\n        bit.add(a, 1)\n\n \
    \   def add_right(self, i):\n        a = A[i]\n        self.inv += bit.sum(a +\
    \ 1, le)\n        bit.add(a, 1)\n\n    def delete_left(self, i):\n        a =\
    \ A[i]\n        self.inv -= bit.sum(a)\n        bit.add(a, -1)\n\n    def delete_right(self,\
    \ i):\n        a = A[i]\n        self.inv -= bit.sum(a + 1, le)\n        bit.add(a,\
    \ -1)\n\n    def rem(self, i):\n        ans[i] = self.inv\n\n\nmo = Mo(n, Q)\n\
    for _ in range(Q):\n    l, r = map(int, input().split())\n    mo.insert(l, r)\n\
    \nle = len(dic)\nbit = BIT(le)\nans = [0] * Q\n\nmo.run()\nprint(*ans, sep=\"\\\
    n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/misc/MoBase_.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/misc/MoBase_.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/misc/MoBase_.test.py
- /verify/expansion/$tests/misc/MoBase_.test.py.html
title: expansion/$tests/misc/MoBase_.test.py
---