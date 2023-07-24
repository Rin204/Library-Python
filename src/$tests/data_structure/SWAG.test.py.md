---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/data_structure/SWAG.py
    title: src/data_structure/SWAG.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/queue_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/queue_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.data_structure.SWAG import SWAG\n\n\nMOD = 998244353\n\n\ndef ope(l,\
    \ r):\n    a = l >> 30\n    b = l ^ (a << 30)\n    c = r >> 30\n    d = r ^ (c\
    \ << 30)\n\n    e = (a * c) % MOD\n    f = (b * c + d) % MOD\n\n    return (e\
    \ << 30) | f\n\n\nQ = int(input())\nswag = SWAG(ope, 1 << 30)\n\nfor _ in range(Q):\n\
    \    query = list(map(int, input().split()))\n    if query[0] == 0:\n        swag.push((query[1]\
    \ << 30) | query[2])\n    elif query[0] == 1:\n        swag.pop()\n    else:\n\
    \        res = swag.prod()\n        a = res >> 30\n        b = res ^ (a << 30)\n\
    \        ans = (a * query[1] + b) % MOD\n        print(ans)\n"
  dependsOn:
  - src/data_structure/SWAG.py
  isVerificationFile: true
  path: src/$tests/data_structure/SWAG.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/data_structure/SWAG.test.py
layout: document
redirect_from:
- /verify/src/$tests/data_structure/SWAG.test.py
- /verify/src/$tests/data_structure/SWAG.test.py.html
title: src/$tests/data_structure/SWAG.test.py
---
