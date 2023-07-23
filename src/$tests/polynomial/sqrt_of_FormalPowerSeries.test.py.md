---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.polynomial.FormalPowerSeries998 import FormalPowerSeries998\n\nFPS =\
    \ FormalPowerSeries998\nn = int(input())\nF = FPS(map(int, input().split()))\n\
    F = F.sqrt()\nif F:\n    print(*F)\nelse:\n    print(-1)\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
layout: document
redirect_from:
- /verify/src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
- /verify/src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py.html
title: src/$tests/polynomial/sqrt_of_FormalPowerSeries.test.py
---
