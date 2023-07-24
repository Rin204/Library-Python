---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/math/Quotients.py
    title: src/math/Quotients.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_quotients
    links:
    - https://judge.yosupo.jp/problem/enumerate_quotients
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_quotients

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.math.Quotients import Quotients



    n = int(input())

    res = Quotients(n)

    print(len(res))

    print(*[x for x, _, _ in res])

    '
  dependsOn:
  - src/math/Quotients.py
  isVerificationFile: true
  path: src/$tests/math/Quotients.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/Quotients.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/Quotients.test.py
- /verify/src/$tests/math/Quotients.test.py.html
title: src/$tests/math/Quotients.test.py
---
