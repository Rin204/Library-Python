---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/queue_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/queue_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\nclass SWAG:\n    def __init__(self, ope, e):\n        self.L = []\n      \
    \  self.R = []\n        self.Lcum = [e]\n        self.Rall = e\n        self.ope\
    \ = ope\n        self.e = e\n\n    def push(self, x):\n        self.R.append(x)\n\
    \        self.Rall = self.ope(self.Rall, x)\n\n    def pop(self):\n        if\
    \ not self.L:\n            while self.R:\n                self.L.append(self.R.pop())\n\
    \                self.Lcum.append(self.ope(self.L[-1], self.Lcum[-1]))\n     \
    \       self.Rall = self.e\n        self.L.pop()\n        self.Lcum.pop()\n\n\
    \    def prod(self):\n        return self.ope(self.Lcum[-1], self.Rall)\n\n  \
    \  def size(self):\n        return len(self.L) + len(self.R)\n\n    def __len__(self):\n\
    \        return self.size()\n\n    def clear(self):\n        self.L = []\n   \
    \     self.R = []\n        self.Lcum = [self.e]\n        self.Rall = self.e\n\n\
    \nMOD = 998244353\n\n\ndef ope(l, r):\n    a = l >> 30\n    b = l ^ (a << 30)\n\
    \    c = r >> 30\n    d = r ^ (c << 30)\n\n    e = (a * c) % MOD\n    f = (b *\
    \ c + d) % MOD\n\n    return (e << 30) | f\n\n\nQ = int(input())\nswag = SWAG(ope,\
    \ 1 << 30)\n\nfor _ in range(Q):\n    query = list(map(int, input().split()))\n\
    \    if query[0] == 0:\n        swag.push((query[1] << 30) | query[2])\n    elif\
    \ query[0] == 1:\n        swag.pop()\n    else:\n        res = swag.prod()\n \
    \       a = res >> 30\n        b = res ^ (a << 30)\n        ans = (a * query[1]\
    \ + b) % MOD\n        print(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/SWAG.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/SWAG.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/SWAG.test.py
- /verify/expansion/$tests/data_structure/SWAG.test.py.html
title: expansion/$tests/data_structure/SWAG.test.py
---