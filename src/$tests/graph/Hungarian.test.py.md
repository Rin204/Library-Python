---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/graph/Hungarian.py
    title: src/graph/Hungarian.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/assignment
    links:
    - https://judge.yosupo.jp/problem/assignment
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/assignment

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.graph.Hungarian import Hungarian



    n = int(input())

    A = [list(map(int, input().split())) for _ in range(n)]

    mi, assign = Hungarian(A)

    print(mi)

    print(*assign)

    '
  dependsOn:
  - src/graph/Hungarian.py
  isVerificationFile: true
  path: src/$tests/graph/Hungarian.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/graph/Hungarian.test.py
layout: document
redirect_from:
- /verify/src/$tests/graph/Hungarian.test.py
- /verify/src/$tests/graph/Hungarian.test.py.html
title: src/$tests/graph/Hungarian.test.py
---
