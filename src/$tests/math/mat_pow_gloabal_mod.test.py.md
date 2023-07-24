---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/math/mat_exp_global_mod.py
    title: src/math/mat_exp_global_mod.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1750
    links:
    - https://yukicoder.me/problems/no/1750
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1750\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.mat_exp_global_mod import mat_exp_global_mod\n\nn, m, T = map(int,\
    \ input().split())\nA = [[0] * n for _ in range(n)]\nB = [0] * n\nB[0] = 1\nfor\
    \ _ in range(m):\n    s, t = map(int, input().split())\n    A[s][t] = 1\n    A[t][s]\
    \ = 1\n\nB = mat_exp_global_mod(A, B, T)\nprint(B[0])\n"
  dependsOn:
  - src/math/mat_exp_global_mod.py
  isVerificationFile: true
  path: src/$tests/math/mat_pow_gloabal_mod.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/mat_pow_gloabal_mod.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/mat_pow_gloabal_mod.test.py
- /verify/src/$tests/math/mat_pow_gloabal_mod.test.py.html
title: src/$tests/math/mat_pow_gloabal_mod.test.py
---
