---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/string/RollingHash.py
    title: src/string/RollingHash.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B&lang=ja\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.string.RollingHash import RollingHash\n\n\nS = input()\nT = input()\n\
    ls = len(S)\nlt = len(T)\nrh1 = RollingHash(S)\nrh2 = RollingHash(T)\nfor i in\
    \ range(ls - lt + 1):\n    if rh1.get(i, i + lt) == rh2.get(0, lt):\n        print(i)\n"
  dependsOn:
  - src/string/RollingHash.py
  isVerificationFile: true
  path: src/$tests/string/RollingHash.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/string/RollingHash.test.py
layout: document
redirect_from:
- /verify/src/$tests/string/RollingHash.test.py
- /verify/src/$tests/string/RollingHash.test.py.html
title: src/$tests/string/RollingHash.test.py
---
