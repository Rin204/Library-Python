---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/math/TwoSAT.py
    title: src/math/TwoSAT.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_sat
    links:
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.TwoSAT import TwoSAT\n\n\n_, _, n, m = input().split()\nn = int(n)\n\
    m = int(m)\nG = TwoSAT(n)\nfor _ in range(m):\n    a, b, _ = map(int, input().split())\n\
    \    G.add_clause(abs(a) - 1, a > 0, abs(b) - 1, b > 0)\n\nif G.check():\n   \
    \ print(\"s SATISFIABLE\")\n    res = G.assign()\n    ans = [\"v\"]\n    for i,\
    \ r in enumerate(res, 1):\n        if r:\n            ans.append(i)\n        else:\n\
    \            ans.append(-i)\n    ans.append(0)\n    print(*ans)\nelse:\n    print(\"\
    s UNSATISFIABLE\")\n"
  dependsOn:
  - src/math/TwoSAT.py
  isVerificationFile: true
  path: src/$tests/math/TwoSAT.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/TwoSAT.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/TwoSAT.test.py
- /verify/src/$tests/math/TwoSAT.test.py.html
title: src/$tests/math/TwoSAT.test.py
---
