---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/convolution/xor_convolution_global_mod.py
    title: src/convolution/xor_convolution_global_mod.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_xor_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_xor_convolution
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.convolution.xor_convolution_global_mod import xor_convolution_global_mod



    n = int(input())

    A = list(map(int, input().split()))

    B = list(map(int, input().split()))

    C = xor_convolution_global_mod(A, B)

    print(*C)

    '
  dependsOn:
  - src/convolution/xor_convolution_global_mod.py
  isVerificationFile: true
  path: src/$tests/convolution/xor_convolution_global.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/convolution/xor_convolution_global.test.py
layout: document
redirect_from:
- /verify/src/$tests/convolution/xor_convolution_global.test.py
- /verify/src/$tests/convolution/xor_convolution_global.test.py.html
title: src/$tests/convolution/xor_convolution_global.test.py
---
