---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/649
    links:
    - https://yukicoder.me/problems/no/649
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/649\n\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.data_structure.BIT import BIT\n\nQ, k = map(int, input().split())\n\
    Query = []\nX = []\nfor _ in range(Q):\n    query = list(map(int, input().split()))\n\
    \    if query[0] == 1:\n        X.append(query[1])\n        Query.append(query[1])\n\
    \    else:\n        Query.append(-1)\n\nX = sorted(set(X))\ndic = {x: i for i,\
    \ x in enumerate(X)}\n\nbit = BIT(len(dic))\nfor q in Query:\n    if q == -1:\n\
    \        p = bit.lower_bound(k) - 1\n        if p == len(X):\n            print(-1)\n\
    \        else:\n            print(X[p])\n            bit.add(p, -1)\n    else:\n\
    \        bit.add(dic[q], 1)\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/data_structure/BIT2.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/BIT2.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/BIT2.test.py
- /verify/src/$tests/data_structure/BIT2.test.py.html
title: src/$tests/data_structure/BIT2.test.py
---
