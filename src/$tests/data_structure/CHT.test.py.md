---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/ConvexHullTrick.py
    title: src/data_structure/ConvexHullTrick.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
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
    from src.data_structure.ConvexHullTrick import ConvexHullTrick\n\n\nn, a, b, w\
    \ = map(int, input().split())\nD = list(map(int, input().split()))\ndp = [0] *\
    \ (n + 1)\ndp[0] = w\n\n\nch = ConvexHullTrick()\nfor i, d in enumerate(D):\n\
    \    ch.add_line(-2 * b * i, 2 * dp[i] + 2 * a * i + b * i * i + b * i)\n    x\
    \ = i + 1\n    mi = ch.get(x)\n    tmp = mi + 2 * a + 2 * d - 2 * a * x + b *\
    \ x * x - b * x\n    dp[x] = tmp // 2\n\nans = 1 << 60\nfor i in range(n + 1):\n\
    \    d = n - i\n    ans = min(ans, dp[i] - a * d + b * d * (d + 1) // 2)\nprint(ans)\n"
  dependsOn:
  - src/data_structure/ConvexHullTrick.py
  isVerificationFile: true
  path: src/$tests/data_structure/CHT.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/CHT.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/CHT.test.py
- /verify/src/$tests/data_structure/CHT.test.py.html
title: src/$tests/data_structure/CHT.test.py
---
