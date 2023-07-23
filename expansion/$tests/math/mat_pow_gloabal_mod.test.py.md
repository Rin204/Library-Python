---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1750
    links:
    - https://yukicoder.me/problems/no/1750
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1750\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    MOD = 998244353\n\n\ndef mat_exp_global_mod(A, B, n):\n    le = len(A)\n    while\
    \ n > 0:\n        if n & 1:\n            C = [0] * le\n            for i in range(le):\n\
    \                for j in range(le):\n                    C[i] += A[i][j] * B[j]\n\
    \                    C[i] %= MOD\n            B = C\n        C = [[0] * le for\
    \ _ in range(le)]\n        for i in range(le):\n            for k in range(le):\n\
    \                for j in range(le):\n                    C[i][j] += A[i][k] *\
    \ A[k][j]\n                    C[i][j] %= MOD\n        A = C\n        n >>= 1\n\
    \n    return B\n\n\nn, m, T = map(int, input().split())\nA = [[0] * n for _ in\
    \ range(n)]\nB = [0] * n\nB[0] = 1\nfor _ in range(m):\n    s, t = map(int, input().split())\n\
    \    A[s][t] = 1\n    A[t][s] = 1\n\nB = mat_exp_global_mod(A, B, T)\nprint(B[0])\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/mat_pow_gloabal_mod.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/mat_pow_gloabal_mod.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/mat_pow_gloabal_mod.test.py
- /verify/expansion/$tests/math/mat_pow_gloabal_mod.test.py.html
title: expansion/$tests/math/mat_pow_gloabal_mod.test.py
---
