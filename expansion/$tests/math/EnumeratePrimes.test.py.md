---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_primes
    links:
    - https://judge.yosupo.jp/problem/enumerate_primes
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_primes\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n\ndef EnumeratePrimes(n):\n    if n <= 1:\n        return []\n    A = [1, 7,\
    \ 11, 13, 17, 19, 23, 29]\n    thres = (n + 29) // 30\n    sieve = [255] * (thres\
    \ + int(n**0.5) + 10)\n\n    def ntoi(i):\n        return (i >> 2) + (not (~i\
    \ & 19))\n\n    sieve[0] ^= 1\n    i = 0\n    flg = 1\n    while flg:\n      \
    \  if sieve[i] != 0:\n            for j in range(8):\n                if sieve[i]\
    \ >> j & 1:\n                    p = i * 30 + A[j]\n                    if p *\
    \ p > n:\n                        flg = 0\n                        continue\n\
    \                    q = [0] * 8\n                    r = [0] * 8\n          \
    \          s = 0\n                    for k in range(8):\n                   \
    \     x = p * (i * 30 + A[k])\n                        q[k] = x // 30\n      \
    \                  r[k] = ntoi(x - 30 * q[k])\n                    while q[0]\
    \ + s < thres:\n                        sieve[q[0] + s] &= ~(1 << r[0])\n    \
    \                    sieve[q[1] + s] &= ~(1 << r[1])\n                       \
    \ sieve[q[2] + s] &= ~(1 << r[2])\n                        sieve[q[3] + s] &=\
    \ ~(1 << r[3])\n                        sieve[q[4] + s] &= ~(1 << r[4])\n    \
    \                    sieve[q[5] + s] &= ~(1 << r[5])\n                       \
    \ sieve[q[6] + s] &= ~(1 << r[6])\n                        sieve[q[7] + s] &=\
    \ ~(1 << r[7])\n                        s += p\n\n        i += 1\n    primes =\
    \ [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n    for i in range(1, thres):\n      \
    \  for j in range(8):\n            if sieve[i] >> j & 1:\n                primes.append(i\
    \ * 30 + A[j])\n    while primes[-1] > n:\n        primes.pop()\n    return primes\n\
    \n\nn, a, b = map(int, input().split())\nprimes = EnumeratePrimes(n)\nle = len(primes)\n\
    ans = []\nfor i in range(b, le, a):\n    ans.append(primes[i])\n\nprint(le, len(ans))\n\
    print(*ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/math/EnumeratePrimes.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/math/EnumeratePrimes.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/math/EnumeratePrimes.test.py
- /verify/expansion/$tests/math/EnumeratePrimes.test.py.html
title: expansion/$tests/math/EnumeratePrimes.test.py
---
