---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/zalgorithm
    links:
    - https://judge.yosupo.jp/problem/zalgorithm
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef Z_algorithm(S):\n    le = len(S)\n    Z = [0] * le\n    Z[0] = le\n  \
    \  i = 1\n    j = 0\n    while i < le:\n        while i + j < le and S[j] == S[i\
    \ + j]:\n            j += 1\n        Z[i] = j\n        if j == 0:\n          \
    \  i += 1\n            continue\n\n        k = 1\n        while i + k < le and\
    \ k + Z[k] < j:\n            Z[i + k] = Z[k]\n            k += 1\n        i +=\
    \ k\n        j -= k\n    return Z\n\n\nS = input()\nres = Z_algorithm(S)\nprint(*res)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/string/Z_algorithm.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/string/Z_algorithm.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/string/Z_algorithm.test.py
- /verify/expansion/$tests/string/Z_algorithm.test.py.html
title: expansion/$tests/string/Z_algorithm.test.py
---
