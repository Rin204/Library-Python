---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/string/RollingHash.py
    title: src/string/RollingHash.py
  - icon: ':x:'
    path: src/string/wildcard_mathing.py
    title: src/string/wildcard_mathing.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/2231
    links:
    - https://yukicoder.me/problems/no/2231
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/2231\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.string.RollingHash import RollingHash\nfrom src.string.wildcard_mathing\
    \ import wildcard_matching\n\n\ndef solve():\n    n, m = map(int, input().split())\n\
    \    S = list(input())\n    T = list(input())\n    res = wildcard_matching(S,\
    \ T)\n    if not res:\n        print(-1)\n        return\n\n    for i in range(n):\n\
    \        if S[i] == \"?\":\n            S[i] = \"a\"\n\n    rhs = RollingHash(S)\n\
    \    rht = RollingHash(T)\n\n    def calc(i, l):\n        if l <= i:\n       \
    \     return rhs.get(0, l)\n        elif l <= i + m:\n            return RollingHash.CalcMod(\n\
    \                RollingHash.Mul(rhs.get(0, i), rhs.pw[l - i]) + rht.get(0, l\
    \ - i)\n            )\n        else:\n            return rhs.get(i + m, l)\n\n\
    \    def get(i, l):\n        if l < i:\n            return S[l]\n        elif\
    \ l < i + m:\n            return T[l - i]\n        else:\n            return S[l]\n\
    \n    ind = res[0]\n    for i in range(1, len(res)):\n        l = 0\n        r\
    \ = n\n        while r - l > 1:\n            mid = (l + r) // 2\n            if\
    \ calc(res[i], mid) == calc(ind, mid):\n                l = mid\n            else:\n\
    \                r = mid\n\n        if get(res[i], l) < get(ind, l):\n       \
    \     ind = res[i]\n\n    for i in range(m):\n        S[i + ind] = T[i]\n    print(*S,\
    \ sep=\"\")\n\n\nfor _ in range(int(input())):\n    solve()\n"
  dependsOn:
  - src/string/RollingHash.py
  - src/string/wildcard_mathing.py
  isVerificationFile: true
  path: src/$tests/string/wildcard_mathing.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/string/wildcard_mathing.test.py
layout: document
redirect_from:
- /verify/src/$tests/string/wildcard_mathing.test.py
- /verify/src/$tests/string/wildcard_mathing.test.py.html
title: src/$tests/string/wildcard_mathing.test.py
---
