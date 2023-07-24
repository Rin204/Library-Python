---
data:
  _extendedDependsOn: []
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
    \n\ndef MillerRabin(n):\n    if n <= 1:\n        return False\n    elif n == 2:\n\
    \        return True\n    elif n % 2 == 0:\n        return False\n\n    if n <\
    \ 4759123141:\n        A = [2, 7, 61]\n    else:\n        A = [2, 325, 9375, 28178,\
    \ 450775, 9780504, 1795265022]\n    s = 0\n    d = n - 1\n    while d % 2 == 0:\n\
    \        s += 1\n        d >>= 1\n\n    for a in A:\n        if a % n == 0:\n\
    \            return True\n        x = pow(a, d, n)\n        if x != 1:\n     \
    \       for t in range(s):\n                if x == n - 1:\n                 \
    \   break\n                x = x * x % n\n            else:\n                return\
    \ False\n    return True\n\n\nQ = int(input())\nfor _ in range(Q):\n    n = int(input())\n\
    \    if MillerRabin(n):\n        print(\"Yes\")\n    else:\n        print(\"No\"\
    )\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/MillerRabin.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/MillerRabin.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/MillerRabin.test.py
- /verify/expansion/$tests/math/MillerRabin.test.py.html
title: expansion/$tests/math/MillerRabin.test.py
---
