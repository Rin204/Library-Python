---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/409
    links:
    - https://yukicoder.me/problems/no/409
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/409\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from collections import deque\n\n\nclass ConvexHullTrick:\n    def __init__(self):\n\
    \        self.deq = deque()\n\n    def check(f1, f2, f3):\n        return (f2[0]\
    \ - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])\n\n    def f(self,\
    \ _f, x):\n        return _f[0] * x + _f[1]\n\n    def add_line(self, a, b):\n\
    \        \"\"\"\n        add  f_i(x) = a * x + b\n        \"\"\"\n        f =\
    \ (a, b)\n        while len(self.deq) >= 2 and ConvexHullTrick.check(self.deq[-2],\
    \ self.deq[-1], f):\n            self.deq.pop()\n        self.deq.append(f)\n\n\
    \    def get(self, x):\n        \"\"\"\n        return min_i f_i(x)\n        \"\
    \"\"\n        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1],\
    \ x):\n            self.deq.popleft()\n\n        return self.f(self.deq[0], x)\n\
    \n\nn, a, b, w = map(int, input().split())\nD = list(map(int, input().split()))\n\
    dp = [0] * (n + 1)\ndp[0] = w\n\n\nch = ConvexHullTrick()\nfor i, d in enumerate(D):\n\
    \    ch.add_line(-2 * b * i, 2 * dp[i] + 2 * a * i + b * i * i + b * i)\n    x\
    \ = i + 1\n    mi = ch.get(x)\n    tmp = mi + 2 * a + 2 * d - 2 * a * x + b *\
    \ x * x - b * x\n    dp[x] = tmp // 2\n\nans = 1 << 60\nfor i in range(n + 1):\n\
    \    d = n - i\n    ans = min(ans, dp[i] - a * d + b * d * (d + 1) // 2)\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/data_structure/CHT.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/data_structure/CHT.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/data_structure/CHT.test.py
- /verify/expansion/$tests/data_structure/CHT.test.py.html
title: expansion/$tests/data_structure/CHT.test.py
---
