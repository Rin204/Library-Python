---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/string/suffix_array.py
    title: src/string/suffix_array.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/suffixarray
    links:
    - https://judge.yosupo.jp/problem/suffixarray
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.string.suffix_array import suffix_array



    S = input()

    sa = suffix_array(S)

    print(*sa)

    '
  dependsOn:
  - src/string/suffix_array.py
  isVerificationFile: true
  path: src/$tests/string/suffix_array.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/string/suffix_array.test.py
layout: document
redirect_from:
- /verify/src/$tests/string/suffix_array.test.py
- /verify/src/$tests/string/suffix_array.test.py.html
title: src/$tests/string/suffix_array.test.py
---
