---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/convolution/or_convolution_global_mod.py
    title: src/convolution/or_convolution_global_mod.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.convolution.or_convolution_global_mod import or_convolution_global_mod\n\
    \n\nn = int(input())\nA = list(map(int, input().split()))\nB = list(map(int, input().split()))\n\
    A_ = [0] * (1 << n)\nB_ = [0] * (1 << n)\nmask = (1 << n) - 1\nfor i in range(1\
    \ << n):\n    A_[i ^ mask] = A[i]\n    B_[i ^ mask] = B[i]\nC_ = or_convolution_global_mod(A_,\
    \ B_)\nC = [0] * (1 << n)\nfor i in range(1 << n):\n    C[i ^ mask] = C_[i]\n\
    print(*C)\n"
  dependsOn:
  - src/convolution/or_convolution_global_mod.py
  isVerificationFile: true
  path: src/$tests/convolution/or_convolution_global.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/convolution/or_convolution_global.test.py
layout: document
redirect_from:
- /verify/src/$tests/convolution/or_convolution_global.test.py
- /verify/src/$tests/convolution/or_convolution_global.test.py.html
title: src/$tests/convolution/or_convolution_global.test.py
---
