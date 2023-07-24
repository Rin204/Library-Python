---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/tree/Kruskal.py
    title: src/tree/Kruskal.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A


    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


    from src.tree.Kruskal import Kruskal


    n, m = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(m)]

    print(Kruskal(n, edges))

    '
  dependsOn:
  - src/tree/Kruskal.py
  isVerificationFile: true
  path: src/$tests/tree/Kruskal.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/tree/Kruskal.test.py
layout: document
redirect_from:
- /verify/src/$tests/tree/Kruskal.test.py
- /verify/src/$tests/tree/Kruskal.test.py.html
title: src/$tests/tree/Kruskal.test.py
---
