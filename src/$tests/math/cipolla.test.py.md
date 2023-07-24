---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/math/cipolla.py
    title: src/math/cipolla.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_mod
    links:
    - https://judge.yosupo.jp/problem/sqrt_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.math.cipolla import cipolla\n\nfor _ in range(int(input())):\n    y,\
    \ p = map(int, input().split())\n    print(cipolla(y, p))\n"
  dependsOn:
  - src/math/cipolla.py
  isVerificationFile: true
  path: src/$tests/math/cipolla.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/math/cipolla.test.py
layout: document
redirect_from:
- /verify/src/$tests/math/cipolla.test.py
- /verify/src/$tests/math/cipolla.test.py.html
title: src/$tests/math/cipolla.test.py
---
