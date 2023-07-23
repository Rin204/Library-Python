---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/polynomial/FormalPowerSeries998.py
    title: src/polynomial/FormalPowerSeries998.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/log_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/log_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/log_of_formal_power_series

    from pathlib import Path

    import sys


    sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

    from src.polynomial.FormalPowerSeries998 import FormalPowerSeries998


    FPS = FormalPowerSeries998

    n = int(input())

    F = FPS(map(int, input().split()))

    print(*F.log())

    '
  dependsOn:
  - src/polynomial/FormalPowerSeries998.py
  isVerificationFile: true
  path: src/$tests/polynomial/log_of_FormalPowerSeries.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/polynomial/log_of_FormalPowerSeries.test.py
layout: document
redirect_from:
- /verify/src/$tests/polynomial/log_of_FormalPowerSeries.test.py
- /verify/src/$tests/polynomial/log_of_FormalPowerSeries.test.py.html
title: src/$tests/polynomial/log_of_FormalPowerSeries.test.py
---
