---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/polynomial/berlekamp_massey_global_mod.py
    title: src/polynomial/berlekamp_massey_global_mod.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/find_linear_recurrence
    links:
    - https://judge.yosupo.jp/problem/find_linear_recurrence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/find_linear_recurrence\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.polynomial.berlekamp_massey_global_mod import berlekamp_massey_global_mod\n\
    \n\nn = int(input())\nif n == 0:\n    A = []\nelse:\n    A = list(map(int, input().split()))\n\
    C = berlekamp_massey_global_mod(A)\nprint(len(C))\nprint(*C)\n"
  dependsOn:
  - src/polynomial/berlekamp_massey_global_mod.py
  isVerificationFile: true
  path: src/$tests/polynomial/berlekamp_massey_global_mod.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/polynomial/berlekamp_massey_global_mod.test.py
layout: document
redirect_from:
- /verify/src/$tests/polynomial/berlekamp_massey_global_mod.test.py
- /verify/src/$tests/polynomial/berlekamp_massey_global_mod.test.py.html
title: src/$tests/polynomial/berlekamp_massey_global_mod.test.py
---
