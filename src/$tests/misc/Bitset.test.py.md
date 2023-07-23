---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1861
    links:
    - https://yukicoder.me/problems/no/1861
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1861\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.misc.Bitset import Bitset\nfrom copy import deepcopy\n\nn, k = map(int,\
    \ input().split())\nA = list(map(int, input().split()))\nB = int(n**0.5)\nbs =\
    \ Bitset(k + 1)\nbs[0] = 1\ndp = [deepcopy(bs)]\nfor i, a in enumerate(A, 1):\n\
    \    bs |= bs << a\n    if i % B == 0:\n        dp.append(deepcopy(bs))\n\nif\
    \ not bs[k]:\n    print(-1)\n    exit()\n\nbit = Bitset(k + 1)\nbit[k] = 1\nans\
    \ = 0\n\np = (n - 1) // B\ndp2 = [dp[p]]\nfor i in range(B * p, n - 1):\n    dp2.append(dp2[-1]\
    \ | (dp2[-1] << A[i]))\n\nfor i in range(n - 1, -1, -1):\n    if bit.and_count(dp2[i\
    \ % B]) == 0:\n        ans += 1\n    if i % B == 0:\n        p = (i - 1) // B\n\
    \        dp2 = [dp[p]]\n        for j in range(B * p, B * (p + 1) - 1):\n    \
    \        dp2.append(dp2[-1] | (dp2[-1] << A[j]))\n    bit |= bit >> A[i]\n\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/misc/Bitset.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/misc/Bitset.test.py
layout: document
redirect_from:
- /verify/src/$tests/misc/Bitset.test.py
- /verify/src/$tests/misc/Bitset.test.py.html
title: src/$tests/misc/Bitset.test.py
---
