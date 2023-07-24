---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/math/MillerRabin.py
    title: src/math/MillerRabin.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/primality_test
    links:
    - https://judge.yosupo.jp/problem/primality_test
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.math.MillerRabin import MillerRabin\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    n = int(input())\n    if MillerRabin(n):\n        print(\"Yes\")\n    else:\n\
    \        print(\"No\")\n"
  dependsOn:
  - src/math/MillerRabin.py
  isVerificationFile: true
  path: src/$tests/math/MillerRabin.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/MillerRabin.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/MillerRabin.test.py
- /verify/src/$tests/math/MillerRabin.test.py.html
title: src/$tests/math/MillerRabin.test.py
---
