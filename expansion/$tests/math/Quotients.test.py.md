---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_quotients
    links:
    - https://judge.yosupo.jp/problem/enumerate_quotients
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_quotients\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef Quotients(n):\n    \"\"\"\n    return [(x_i, l_i, r_i), ...]\n    s.t.\
    \ (n / i) == x \\\\forall i \\\\in [l, r), x_i < x_{i+1}\n    \"\"\"\n\n    ret\
    \ = []\n    l = 1\n    while l <= n:\n        p = n // l\n        r = n // p +\
    \ 1\n        ret.append((p, l, r))\n        l = r\n    return ret[::-1]\n\n\n\
    n = int(input())\nres = Quotients(n)\nprint(len(res))\nprint(*[x for x, _, _ in\
    \ res])\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/Quotients.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/Quotients.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/Quotients.test.py
- /verify/expansion/$tests/math/Quotients.test.py.html
title: expansion/$tests/math/Quotients.test.py
---