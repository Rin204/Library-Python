---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/find_linear_recurrence
    links:
    - https://judge.yosupo.jp/problem/find_linear_recurrence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/find_linear_recurrence\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.polynomial.berlekamp_massey_global_mod import berlekamp_massey_global_mod\n\
    \n\nn = int(input())\nif n == 0:\n    A = []\nelse:\n    A = list(map(int, input().split()))\n\
    C = berlekamp_massey_global_mod(A)\nprint(len(C))\nprint(*C)\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/polynomial/berlekamp_massey_global_mod.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/polynomial/berlekamp_massey_global_mod.test.py
layout: document
redirect_from:
- /verify/src/$tests/polynomial/berlekamp_massey_global_mod.test.py
- /verify/src/$tests/polynomial/berlekamp_massey_global_mod.test.py.html
title: src/$tests/polynomial/berlekamp_massey_global_mod.test.py
---
