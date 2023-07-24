---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/math/Combination.py
    title: src/math/Combination.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
    links:
    - https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.Combination import Combination\n\n\nT, MOD = map(int, input().split())\n\
    # \u52DD\u624B\u306B\u30C6\u30FC\u30D6\u30EB\u3092\u62E1\u5F35\u3057\u3066\u304F\
    \u308C\u308B\u30C6\u30B9\u30C8\nC = Combination(min(MOD - 1, 100000), MOD)\n\n\
    for _ in range(T):\n    n, k = map(int, input().split())\n    print(C.nCk(n, k))\n"
  dependsOn:
  - src/math/Combination.py
  isVerificationFile: true
  path: src/$tests/math/Combination.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/Combination.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/Combination.test.py
- /verify/src/$tests/math/Combination.test.py.html
title: src/$tests/math/Combination.test.py
---
