---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/187
    links:
    - https://yukicoder.me/problems/no/187
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/187\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.Garner import Garner\n\n\nn = int(input())\nR = [0] * n\nM = [0]\
    \ * n\nfor i in range(n):\n    R[i], M[i] = map(int, input().split())\n\nr, m\
    \ = Garner(R, M)\nif r == -1:\n    print(-1)\nelse:\n    if r == 0:\n        r\
    \ = m\n    print(r % (10**9 + 7))\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/math/Garner.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/Garner.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/Garner.test.py
- /verify/src/$tests/math/Garner.test.py.html
title: src/$tests/math/Garner.test.py
---
