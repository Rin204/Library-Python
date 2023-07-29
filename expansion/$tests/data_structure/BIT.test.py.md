---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
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
    \ //= 2\n        return i + 1\n\n\nn, Q = map(int, input().split())\nbit = BIT(n)\n\
    for _ in range(Q):\n    t, x, y = map(int, input().split())\n    if t == 0:\n\
    \        bit.add(x - 1, y)\n    else:\n        print(bit.sum(x - 1, y))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/BIT.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/BIT.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/BIT.test.py
- /verify/expansion/$tests/data_structure/BIT.test.py.html
title: expansion/$tests/data_structure/BIT.test.py
---