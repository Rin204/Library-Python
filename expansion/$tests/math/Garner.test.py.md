---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/187
    links:
    - https://yukicoder.me/problems/no/187
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/187\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef ext_gcd(a, b):\n    \"\"\"\n    return (x, y, gcd(a, b)) s.t. ax + by\
    \ = gcd(a, b)\n    \"\"\"\n    if b == 0:\n        return 1, 0, a\n    else:\n\
    \        y, x, g = ext_gcd(b, a % b)\n        return x, y - (a // b) * x, g\n\n\
    \ndef Garner(R, M):\n    r = 0\n    m = 1\n    for ri, mi in zip(R, M):\n    \
    \    if ri < 0 or mi <= ri:\n            ri %= mi\n\n        if m < mi:\n    \
    \        m, mi = mi, m\n            r, ri = ri, r\n\n        if m % mi == 0:\n\
    \            if r % mi != ri:\n                return -1, -1\n            continue\n\
    \n        im, _, g = ext_gcd(m, mi)\n        if im < 0:\n            im += mi\n\
    \n        if (ri - r) % g != 0:\n            return -1, -1\n\n        ui = mi\
    \ // g\n        x = ((ri - r) // g % ui) * im % ui\n        r += x * m\n     \
    \   m *= ui\n\n    return r, m\n\n\nn = int(input())\nR = [0] * n\nM = [0] * n\n\
    for i in range(n):\n    R[i], M[i] = map(int, input().split())\n\nr, m = Garner(R,\
    \ M)\nif r == -1:\n    print(-1)\nelse:\n    if r == 0:\n        r = m\n    print(r\
    \ % (10**9 + 7))\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/Garner.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/Garner.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/Garner.test.py
- /verify/expansion/$tests/math/Garner.test.py.html
title: expansion/$tests/math/Garner.test.py
---
