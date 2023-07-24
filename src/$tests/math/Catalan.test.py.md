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
    PROBLEM: https://yukicoder.me/problems/no/790
    links:
    - https://yukicoder.me/problems/no/790
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://yukicoder.me/problems/no/790

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.math.Combination import Combination



    n = int(input())

    C = Combination(n)

    print(C.Catalan(n))

    '
  dependsOn:
  - src/math/Combination.py
  isVerificationFile: true
  path: src/$tests/math/Catalan.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/Catalan.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/Catalan.test.py
- /verify/src/$tests/math/Catalan.test.py.html
title: src/$tests/math/Catalan.test.py
---
