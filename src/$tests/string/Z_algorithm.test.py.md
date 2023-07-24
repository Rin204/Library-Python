---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/string/Z_algorithm.py
    title: src/string/Z_algorithm.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
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
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.string.Z_algorithm import Z_algorithm


    S = input()

    res = Z_algorithm(S)

    print(*res)

    '
  dependsOn:
  - src/string/Z_algorithm.py
  isVerificationFile: true
  path: src/$tests/string/Z_algorithm.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/string/Z_algorithm.test.py
layout: document
redirect_from:
- /verify/src/$tests/string/Z_algorithm.test.py
- /verify/src/$tests/string/Z_algorithm.test.py.html
title: src/$tests/string/Z_algorithm.test.py
---
