---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/RollbackUnionFind.py
    title: src/data_structure/RollbackUnionFind.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1293
    links:
    - https://yukicoder.me/problems/no/1293
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1293\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.data_structure.RollbackUnionFind import RollbackUnionFind\n\n\nn, d,\
    \ w = map(int, input().split())\nUF1 = RollbackUnionFind(n)\nUF2 = RollbackUnionFind(n)\n\
    for _ in range(d):\n    a, b = map(int, input().split())\n    UF1.unite(a - 1,\
    \ b - 1)\nfor _ in range(w):\n    c, d = map(int, input().split())\n    UF2.unite(c\
    \ - 1, d - 1)\n\nans = -n\ndic = {}\nfor i in range(n):\n    p = UF1.find(i)\n\
    \    if p not in dic:\n        dic[p] = []\n    dic[p].append(i)\n\nfor group\
    \ in dic.values():\n    u = group[0]\n    state = UF2.get_state()\n    for v in\
    \ group:\n        UF2.unite(u, v)\n    ans += UF1.size(u) * UF2.size(u)\n    UF2.rollback(state)\n\
    \nprint(ans)\n"
  dependsOn:
  - src/data_structure/RollbackUnionFind.py
  isVerificationFile: true
  path: src/$tests/data_structure/RollbackUF.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/RollbackUF.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/RollbackUF.test.py
- /verify/src/$tests/data_structure/RollbackUF.test.py.html
title: src/$tests/data_structure/RollbackUF.test.py
---
