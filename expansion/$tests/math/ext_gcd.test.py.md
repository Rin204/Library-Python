---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef ext_gcd(a, b):\n    \"\"\"\n    return (x, y, gcd(a, b)) s.t. ax + by\
    \ = gcd(a, b)\n    \"\"\"\n    if b == 0:\n        return 1, 0, a\n    else:\n\
    \        y, x, g = ext_gcd(b, a % b)\n        return x, y - (a // b) * x, g\n\n\
    \na, b = map(int, input().split())\nx, y, g = ext_gcd(a, b)\nprint(x, y)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/ext_gcd.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/ext_gcd.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/ext_gcd.test.py
- /verify/expansion/$tests/math/ext_gcd.test.py.html
title: expansion/$tests/math/ext_gcd.test.py
---
