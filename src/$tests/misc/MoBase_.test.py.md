---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_inversions_query
    links:
    - https://judge.yosupo.jp/problem/static_range_inversions_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.misc.MoBase_ import MoBase_\nfrom src.data_structure.BIT import BIT\n\
    import sys\n\ninput = sys.stdin.readline\n\nn, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\ndic = {a: i for i, a in enumerate(sorted(set(A)))}\n\
    A = [dic[a] for a in A]\n\n\nclass Mo(MoBase_):\n    def __init__(self, n, Q):\n\
    \        super().__init__(n, Q)\n        self.inv = 0\n\n    def add_left(self,\
    \ i):\n        a = A[i]\n        self.inv += bit.sum(a)\n        bit.add(a, 1)\n\
    \n    def add_right(self, i):\n        a = A[i]\n        self.inv += bit.sum(a\
    \ + 1, le)\n        bit.add(a, 1)\n\n    def delete_left(self, i):\n        a\
    \ = A[i]\n        self.inv -= bit.sum(a)\n        bit.add(a, -1)\n\n    def delete_right(self,\
    \ i):\n        a = A[i]\n        self.inv -= bit.sum(a + 1, le)\n        bit.add(a,\
    \ -1)\n\n    def rem(self, i):\n        ans[i] = self.inv\n\n\nmo = Mo(n, Q)\n\
    for _ in range(Q):\n    l, r = map(int, input().split())\n    mo.insert(l, r)\n\
    \nle = len(dic)\nbit = BIT(le)\nans = [0] * Q\n\nmo.run()\nprint(*ans, sep=\"\\\
    n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/misc/MoBase_.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/misc/MoBase_.test.py
layout: document
redirect_from:
- /verify/src/$tests/misc/MoBase_.test.py
- /verify/src/$tests/misc/MoBase_.test.py.html
title: src/$tests/misc/MoBase_.test.py
---
