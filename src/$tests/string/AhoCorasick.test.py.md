---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/string/AhoCorasick.py
    title: src/string/AhoCorasick.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://yukicoder.me/problems/1013
    links:
    - https://yukicoder.me/problems/1013
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/1013\nfrom pathlib\
    \ import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.string.AhoCorasick import AhoCorasick\n\n\nS = input()\nn = int(input())\n\
    ac = AhoCorasick()\nfor i in range(n):\n    T = input()\n    ac.register(T)\n\n\
    ac.build()\nmatch = ac.search(S)\nls = len(S)\nans = 0\nfor row in match:\n  \
    \  ans += len(row)\n\nprint(ans)\n"
  dependsOn:
  - src/string/AhoCorasick.py
  isVerificationFile: true
  path: src/$tests/string/AhoCorasick.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/string/AhoCorasick.test.py
layout: document
redirect_from:
- /verify/src/$tests/string/AhoCorasick.test.py
- /verify/src/$tests/string/AhoCorasick.test.py.html
title: src/$tests/string/AhoCorasick.test.py
---
