---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/math/EnumeratePrimes.py
    title: src/math/EnumeratePrimes.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_primes
    links:
    - https://judge.yosupo.jp/problem/enumerate_primes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_primes\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.EnumeratePrimes import EnumeratePrimes\n\n\nn, a, b = map(int, input().split())\n\
    primes = EnumeratePrimes(n)\nle = len(primes)\nans = []\nfor i in range(b, le,\
    \ a):\n    ans.append(primes[i])\n\nprint(le, len(ans))\nprint(*ans)\n"
  dependsOn:
  - src/math/EnumeratePrimes.py
  isVerificationFile: true
  path: src/$tests/math/EnumeratePrimes.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/EnumeratePrimes.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/EnumeratePrimes.test.py
- /verify/src/$tests/math/EnumeratePrimes.test.py.html
title: src/$tests/math/EnumeratePrimes.test.py
---
