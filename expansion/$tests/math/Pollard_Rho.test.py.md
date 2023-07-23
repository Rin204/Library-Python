---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/factorize
    links:
    - https://judge.yosupo.jp/problem/factorize
    - https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize\n\
    \nfrom pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom math import gcd\n\n\ndef MillerRabin(n):\n    if n <= 1:\n        return\
    \ False\n    elif n == 2:\n        return True\n    elif n % 2 == 0:\n       \
    \ return False\n\n    if n < 4759123141:\n        A = [2, 7, 61]\n    else:\n\
    \        A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]\n    s = 0\n \
    \   d = n - 1\n    while d % 2 == 0:\n        s += 1\n        d >>= 1\n\n    for\
    \ a in A:\n        if a % n == 0:\n            return True\n        x = pow(a,\
    \ d, n)\n        if x != 1:\n            for t in range(s):\n                if\
    \ x == n - 1:\n                    break\n                x = x * x % n\n    \
    \        else:\n                return False\n    return True\n\n\ndef pollard(n):\n\
    \    # https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a\n\n    if n % 2 ==\
    \ 0:\n        return 2\n\n    m = int(n**0.125) + 1\n    step = 0\n\n    while\
    \ 1:\n        step += 1\n\n        def f(x):\n            return (x * x + step)\
    \ % n\n\n        y = k = 0\n        g = q = r = 1\n\n        while g == 1:\n \
    \           x = y\n            while k < 3 * r // 4:\n                y = f(y)\n\
    \                k += 1\n            while k < r and g == 1:\n               \
    \ ys = y\n                for _ in range(min(m, r - k)):\n                   \
    \ y = f(y)\n                    q = q * abs(x - y) % n\n                g = gcd(q,\
    \ n)\n                k += m\n            k = r\n            r <<= 1\n\n     \
    \   if g == n:\n            g = 1\n            y = ys\n            while g ==\
    \ 1:\n                y = f(y)\n                g = gcd(abs(x - y), n)\n\n   \
    \     if g == n:\n            continue\n        if MillerRabin(g):\n         \
    \   return g\n        elif MillerRabin(n // g):\n            return n // g\n \
    \       else:\n            return pollard(g)\n\n\ndef primefact(n):\n    res =\
    \ []\n    while n > 1 and not MillerRabin(n):\n        p = pollard(n)\n      \
    \  while n % p == 0:\n            res.append(p)\n            n //= p\n    if n\
    \ != 1:\n        res.append(n)\n    return sorted(res)\n\n\ndef primedict(n):\n\
    \    P = primefact(n)\n    ret = {}\n    for p in P:\n        ret[p] = ret.get(p,\
    \ 0) + 1\n    return ret\n\n\nQ = int(input())\nfor _ in range(Q):\n    n = int(input())\n\
    \    P = primefact(n)\n    print(len(P), *P)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/Pollard_Rho.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/Pollard_Rho.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/Pollard_Rho.test.py
- /verify/expansion/$tests/math/Pollard_Rho.test.py.html
title: expansion/$tests/math/Pollard_Rho.test.py
---
