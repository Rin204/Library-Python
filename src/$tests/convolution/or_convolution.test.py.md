---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.convolution.or_convolution import or_convolution\n\n\nn = int(input())\n\
    A = list(map(int, input().split()))\nB = list(map(int, input().split()))\nA_ =\
    \ [0] * (1 << n)\nB_ = [0] * (1 << n)\nmask = (1 << n) - 1\nfor i in range(1 <<\
    \ n):\n    A_[i ^ mask] = A[i]\n    B_[i ^ mask] = B[i]\nC_ = or_convolution(A_,\
    \ B_, 998244353)\nC = [0] * (1 << n)\nfor i in range(1 << n):\n    C[i ^ mask]\
    \ = C_[i]\nprint(*C)\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/convolution/or_convolution.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/convolution/or_convolution.test.py
layout: document
redirect_from:
- /verify/src/$tests/convolution/or_convolution.test.py
- /verify/src/$tests/convolution/or_convolution.test.py.html
title: src/$tests/convolution/or_convolution.test.py
---
