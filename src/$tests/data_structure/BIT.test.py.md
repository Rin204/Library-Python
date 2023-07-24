---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/BIT.py
    title: src/data_structure/BIT.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.data_structure.BIT import BIT\n\nn, Q = map(int, input().split())\n\
    bit = BIT(n)\nfor _ in range(Q):\n    t, x, y = map(int, input().split())\n  \
    \  if t == 0:\n        bit.add(x - 1, y)\n    else:\n        print(bit.sum(x -\
    \ 1, y))\n"
  dependsOn:
  - src/data_structure/BIT.py
  isVerificationFile: true
  path: src/$tests/data_structure/BIT.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/BIT.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/BIT.test.py
- /verify/src/$tests/data_structure/BIT.test.py.html
title: src/$tests/data_structure/BIT.test.py
---
