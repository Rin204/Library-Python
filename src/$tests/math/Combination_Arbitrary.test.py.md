---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/math/CombinationArbitrary.py
    title: src/math/CombinationArbitrary.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/binomial_coefficient
    links:
    - https://judge.yosupo.jp/problem/binomial_coefficient
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.CombinationArbitrary import CombinationArbitrary\n\n\nT, MOD = map(int,\
    \ input().split())\nComb = CombinationArbitrary(MOD)\nfor _ in range(T):\n   \
    \ n, k = map(int, input().split())\n    print(Comb.nCk(n, k))\n"
  dependsOn:
  - src/math/CombinationArbitrary.py
  isVerificationFile: true
  path: src/$tests/math/Combination_Arbitrary.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/Combination_Arbitrary.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/Combination_Arbitrary.test.py
- /verify/src/$tests/math/Combination_Arbitrary.test.py.html
title: src/$tests/math/Combination_Arbitrary.test.py
---
