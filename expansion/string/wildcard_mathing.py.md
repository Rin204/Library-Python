---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\n\n\nclass NTT998:\n    # fmt: off\n    rate2=(0, 911660635,\
    \ 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924,\
    \ 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778,\
    \ 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 867605899,\
    \ 0)\n    irate2=(0, 86583718, 372528824, 373294451, 645684063, 112220581, 692852209,\
    \ 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171,\
    \ 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183,\
    \ 824071951, 103369235, 0)\n    rate3=(0, 372528824, 337190230, 454590761, 816400692,\
    \ 578227951, 180142363, 83780245, 6597683, 70046822, 623238099, 183021267, 402682409,\
    \ 631680428, 344509872, 689220186, 365017329, 774342554, 729444058, 102986190,\
    \ 128751033, 395565204, 0)\n    irate3=(0, 509520358, 929031873, 170256584, 839780419,\
    \ 282974284, 395914482, 444904435, 72135471, 638914820, 66769500, 771127074, 985925487,\
    \ 262319669, 262341272, 625870173, 768022760, 859816005, 914661783, 430819711,\
    \ 272774365, 530924681, 0)\n    # fmt: on\n\n    def butterfly(A):\n        n\
    \ = len(A)\n        h = (n - 1).bit_length()\n        le = 0\n        while le\
    \ < h:\n            if h - le == 1:\n                p = 1 << (h - le - 1)\n \
    \               rot = 1\n                for s in range(1 << le):\n          \
    \          offset = s << (h - le)\n                    for i in range(p):\n  \
    \                      l = A[i + offset]\n                        r = A[i + offset\
    \ + p] * rot\n                        A[i + offset] = (l + r) % 998244353\n  \
    \                      A[i + offset + p] = (l - r) % 998244353\n             \
    \       rot *= NTT998.rate2[(~s & -~s).bit_length()]\n                    rot\
    \ %= 998244353\n                le += 1\n            else:\n                p\
    \ = 1 << (h - le - 2)\n                rot = 1\n                for s in range(1\
    \ << le):\n                    rot2 = rot * rot % 998244353\n                \
    \    rot3 = rot2 * rot % 998244353\n                    offset = s << (h - le)\n\
    \                    for i in range(p):\n                        a0 = A[i + offset]\n\
    \                        a1 = A[i + offset + p] * rot\n                      \
    \  a2 = A[i + offset + p * 2] * rot2\n                        a3 = A[i + offset\
    \ + p * 3] * rot3\n                        a1na3imag = (a1 - a3) % 998244353 *\
    \ 911660635\n                        A[i + offset] = (a0 + a2 + a1 + a3) % 998244353\n\
    \                        A[i + offset + p] = (a0 + a2 - a1 - a3) % 998244353\n\
    \                        A[i + offset + p * 2] = (a0 - a2 + a1na3imag) % 998244353\n\
    \                        A[i + offset + p * 3] = (a0 - a2 - a1na3imag) % 998244353\n\
    \                    rot *= NTT998.rate3[(~s & -~s).bit_length()]\n          \
    \          rot %= 998244353\n                le += 2\n\n    def butterfly_inv(A):\n\
    \        n = len(A)\n        h = (n - 1).bit_length()\n        le = h\n      \
    \  while le:\n            if le == 1:\n                p = 1 << (h - le)\n   \
    \             irot = 1\n                for s in range(1 << (le - 1)):\n     \
    \               offset = s << (h - le + 1)\n                    for i in range(p):\n\
    \                        l = A[i + offset]\n                        r = A[i +\
    \ offset + p]\n                        A[i + offset] = (l + r) % 998244353\n \
    \                       A[i + offset + p] = (l - r) * irot % 998244353\n     \
    \               irot *= NTT998.irate2[(~s & -~s).bit_length()]\n             \
    \       irot %= 998244353\n                le -= 1\n            else:\n      \
    \          p = 1 << (h - le)\n                irot = 1\n                for s\
    \ in range(1 << (le - 2)):\n                    irot2 = irot * irot % 998244353\n\
    \                    irot3 = irot2 * irot % 998244353\n                    offset\
    \ = s << (h - le + 2)\n                    for i in range(p):\n              \
    \          a0 = A[i + offset]\n                        a1 = A[i + offset + p]\n\
    \                        a2 = A[i + offset + p * 2]\n                        a3\
    \ = A[i + offset + p * 3]\n                        a2na3iimag = (a2 - a3) * 86583718\
    \ % 998244353\n                        A[i + offset] = (a0 + a1 + a2 + a3) % 998244353\n\
    \                        A[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % 998244353\n\
    \                        A[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 %\
    \ 998244353\n                        A[i + offset + p * 3] = (a0 - a1 - a2na3iimag)\
    \ * irot3 % 998244353\n                    irot *= NTT998.irate3[(~s & -~s).bit_length()]\n\
    \                    irot %= 998244353\n                le -= 2\n\n    def multiply(A,\
    \ B):\n        n = len(A)\n        m = len(B)\n        if min(n, m) <= 60:\n \
    \           C = [0] * (n + m - 1)\n            for i in range(n):\n          \
    \      if i % 8 == 0:\n                    for j in range(m):\n              \
    \          C[i + j] += A[i] * B[j]\n                        C[i + j] %= 998244353\n\
    \                else:\n                    for j in range(m):\n             \
    \           C[i + j] += A[i] * B[j]\n            return [c % 998244353 for c in\
    \ C]\n        A = A[:]\n        B = B[:]\n        z = 1 << (n + m - 2).bit_length()\n\
    \        A += [0] * (z - n)\n        B += [0] * (z - m)\n        NTT998.butterfly(A)\n\
    \        NTT998.butterfly(B)\n        for i in range(z):\n            A[i] *=\
    \ B[i]\n            A[i] %= 998244353\n        NTT998.butterfly_inv(A)\n     \
    \   A = A[: n + m - 1]\n        iz = pow(z, 998244353 - 2, 998244353)\n      \
    \  return [a * iz % 998244353 for a in A]\n\n\ndef wildcard_matching(S, T, wild=\"\
    ?\"):\n    n = len(S)\n    m = len(T)\n    A = [0] * n\n    B = [0] * m\n    dic\
    \ = {wild: 0}\n    for i, s in enumerate(S):\n        if s not in dic:\n     \
    \       dic[s] = random.randrange(998244353)\n        A[i] = dic[s]\n    for i,\
    \ t in enumerate(T):\n        if t not in dic:\n            dic[t] = random.randrange(998244353)\n\
    \        B[i] = dic[t]\n\n    S1 = [0] * n\n    S2 = [0] * n\n    S3 = [0] * n\n\
    \    for i, x in enumerate(A):\n        y = int(x > 0)\n        S1[i] = y\n  \
    \      S2[i] = y * x\n        S3[i] = y * x * x % 998244353\n\n    T1 = [0] *\
    \ m\n    T2 = [0] * m\n    T3 = [0] * m\n    for i, x in enumerate(B):\n     \
    \   y = int(x > 0)\n        T1[m - 1 - i] = y\n        T2[m - 1 - i] = y * x\n\
    \        T3[m - 1 - i] = y * x * x % 998244353\n\n    res1 = NTT998.multiply(S3,\
    \ T1)\n    res2 = NTT998.multiply(S2, T2)\n    res3 = NTT998.multiply(S1, T3)\n\
    \    res = []\n    for i in range(n - m + 1):\n        x = res1[i + m - 1] - 2\
    \ * res2[i + m - 1] + res3[i + m - 1]\n        if x == 0:\n            res.append(i)\n\
    \n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/string/wildcard_mathing.py
  requiredBy: []
  timestamp: '2023-07-17 18:11:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/string/wildcard_mathing.py
layout: document
redirect_from:
- /library/expansion/string/wildcard_mathing.py
- /library/expansion/string/wildcard_mathing.py.html
title: expansion/string/wildcard_mathing.py
---