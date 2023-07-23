---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_mod
    links:
    - https://judge.yosupo.jp/problem/sqrt_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef cipolla(x, MOD):\n    if MOD == 2:\n        return x\n    elif x == 0:\n\
    \        return 0\n    elif pow(x, (MOD - 1) // 2, MOD) != 1:\n        return\
    \ -1\n\n    y = 1\n    while pow((y * y - x) % MOD, (MOD - 1) // 2, MOD) == 1:\n\
    \        y += 1\n\n    base = (y * y - x) % MOD\n\n    def multi(a0, b0, a1, b1):\n\
    \        return (a0 * a1 + base * (b0 * b1 % MOD)) % MOD, (a0 * b1 + a1 * b0)\
    \ % MOD\n\n    def pow_(a, b, n):\n        if n == 0:\n            return 1, 0\n\
    \n        tmp = multi(a, b, a, b)\n        ret = pow_(tmp[0], tmp[1], n >> 1)\n\
    \        if n & 1:\n            ret = multi(ret[0], ret[1], a, b)\n\n        return\
    \ ret\n\n    return pow_(y, 1, (MOD + 1) // 2)[0]\n\n\nfor _ in range(int(input())):\n\
    \    y, p = map(int, input().split())\n    print(cipolla(y, p))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/cipolla.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/cipolla.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/cipolla.test.py
- /verify/expansion/$tests/math/cipolla.test.py.html
title: expansion/$tests/math/cipolla.test.py
---
