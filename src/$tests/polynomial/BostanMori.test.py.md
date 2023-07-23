---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/convolution/NTT998.py
    title: src/convolution/NTT998.py
  - icon: ':x:'
    path: src/polynomial/BostanMori998.py
    title: src/polynomial/BostanMori998.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence
    links:
    - https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.convolution.NTT998 import NTT998

    from src.polynomial.BostanMori998 import BostanMori998



    d, k = map(int, input().split())

    A = list(map(int, input().split()))

    C = [1] + [-c for c in map(int, input().split())]

    P = NTT998.multiply(A, C)

    P = P[:d]

    ans = BostanMori998(P, C, k)

    print(ans)

    '
  dependsOn:
  - src/convolution/NTT998.py
  - src/polynomial/BostanMori998.py
  isVerificationFile: true
  path: src/$tests/polynomial/BostanMori.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/polynomial/BostanMori.test.py
layout: document
redirect_from:
- /verify/src/$tests/polynomial/BostanMori.test.py
- /verify/src/$tests/polynomial/BostanMori.test.py.html
title: src/$tests/polynomial/BostanMori.test.py
---
