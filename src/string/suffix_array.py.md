---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/string/lcp_array.test.py
    title: src/$tests/string/lcp_array.test.py
  - icon: ''
    path: src/$tests/string/suffix_array.test.py
    title: src/$tests/string/suffix_array.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from functools import cmp_to_key\n\n\ndef sa_naive(S):\n    n = len(S)\n\
    \    sa = [i for i in range(n)]\n\n    def cmp(l, r):\n        if l == r:\n  \
    \          return 0\n        while l < n and r < n:\n            if S[l] != S[r]:\n\
    \                return 1 - 2 * (S[l] < S[r])\n            l += 1\n          \
    \  r += 1\n        return 1 - 2 * (l == n)\n\n    return sorted(sa, key=cmp_to_key(cmp))\n\
    \n\ndef sa_doubling(S):\n    n = len(S)\n    sa = [i for i in range(n)]\n    rnk\
    \ = S[:]\n    tmp = [0] * n\n    k = 1\n    while k < n:\n\n        def cmp(x,\
    \ y):\n            if rnk[x] != rnk[y]:\n                return 1 - 2 * (rnk[x]\
    \ < rnk[y])\n\n            rx = -1\n            if x + k < n:\n              \
    \  rx = rnk[x + k]\n            ry = -1\n            if y + k < n:\n         \
    \       ry = rnk[y + k]\n            return 1 - 2 * (rx < ry)\n\n        sa.sort(key=cmp_to_key(cmp))\n\
    \        tmp[sa[0]] = 0\n        for i in range(n):\n            tmp[sa[i]] =\
    \ tmp[sa[i - 1]] + (1 if cmp(sa[i - 1], sa[i]) == -1 else 0)\n        tmp, rnk\
    \ = rnk, tmp\n        k <<= 1\n\n    return sa\n\n\ndef sa_is(S, upper, NAIVE_THR=10,\
    \ DOUBLING_THR=40):\n    n = len(S)\n    if n == 0:\n        return []\n    elif\
    \ n == 1:\n        return [0]\n    elif n == 2:\n        if S[0] < S[1]:\n   \
    \         return [0, 1]\n        else:\n            return [1, 0]\n    elif n\
    \ <= NAIVE_THR:\n        return sa_naive(S)\n    elif n <= DOUBLING_THR:\n   \
    \     return sa_doubling(S)\n\n    sa = [0] * n\n    ls = [False] * n\n    for\
    \ i in range(n - 2, -1, -1):\n        if S[i] == S[i + 1]:\n            ls[i]\
    \ = ls[i + 1]\n        else:\n            ls[i] = S[i] < S[i + 1]\n\n    sum_l\
    \ = [0] * (upper + 1)\n    sum_s = [0] * (upper + 1)\n\n    for i in range(n):\n\
    \        if not ls[i]:\n            sum_s[S[i]] += 1\n        else:\n        \
    \    sum_l[S[i] + 1] += 1\n\n    for i in range(upper + 1):\n        sum_s[i]\
    \ += sum_l[i]\n        if i < upper:\n            sum_l[i + 1] += sum_s[i]\n\n\
    \    def induce(lms):\n        nonlocal sa\n        sa = [-1] * n\n        buf\
    \ = sum_s[:]\n        for d in lms:\n            if d == n:\n                continue\n\
    \            sa[buf[S[d]]] = d\n            buf[S[d]] += 1\n\n        buf = sum_l[:]\n\
    \        sa[buf[S[n - 1]]] = n - 1\n        buf[S[n - 1]] += 1\n        for i\
    \ in range(n):\n            v = sa[i]\n            if v >= 1 and not ls[v - 1]:\n\
    \                sa[buf[S[v - 1]]] = v - 1\n                buf[S[v - 1]] += 1\n\
    \n        buf = sum_l[:]\n        for i in range(n - 1, -1, -1):\n           \
    \ v = sa[i]\n            if v >= 1 and ls[v - 1]:\n                buf[S[v - 1]\
    \ + 1] -= 1\n                sa[buf[S[v - 1] + 1]] = v - 1\n\n    lms_map = [-1]\
    \ * (n + 1)\n    m = 0\n    lms = []\n    for i in range(1, n):\n        if not\
    \ ls[i - 1] and ls[i]:\n            lms_map[i] = m\n            m += 1\n     \
    \       lms.append(i)\n\n    induce(lms)\n\n    if m > 0:\n        sorted_lms\
    \ = []\n        for v in sa:\n            if lms_map[v] != -1:\n             \
    \   sorted_lms.append(v)\n        rec_s = [0] * m\n        rec_upper = 0\n   \
    \     rec_s[lms_map[sorted_lms[0]]] = 0\n        for i in range(1, m):\n     \
    \       l = sorted_lms[i - 1]\n            r = sorted_lms[i]\n\n            end_l\
    \ = n\n            if lms_map[l] + 1 < m:\n                end_l = lms[lms_map[l]\
    \ + 1]\n            end_r = n\n            if lms_map[r] + 1 < m:\n          \
    \      end_r = lms[lms_map[r] + 1]\n\n            same = True\n            if\
    \ end_l - l != end_r - r:\n                same = False\n            else:\n \
    \               while l < end_l:\n                    if S[l] != S[r]:\n     \
    \                   break\n                    l += 1\n                    r +=\
    \ 1\n                if l == n or S[l] != S[r]:\n                    same = False\n\
    \n            if not same:\n                rec_upper += 1\n            rec_s[lms_map[sorted_lms[i]]]\
    \ = rec_upper\n\n        rec_sa = sa_is(rec_s, rec_upper, NAIVE_THR, DOUBLING_THR)\n\
    \        for i in range(m):\n            sorted_lms[i] = lms[rec_sa[i]]\n\n  \
    \      induce(sorted_lms)\n\n    return sa\n\n\ndef suffix_array(S, NAIVE_THR=10,\
    \ DOUBLING_THR=40):\n    dic = {s: i for i, s in enumerate(sorted(set(S)))}\n\
    \    return sa_is([dic[s] for s in S], len(dic), NAIVE_THR, DOUBLING_THR)\n\n\n\
    def lcp_array(S, sa):\n    n = len(S)\n    rnk = [0] * n\n    for i, s in enumerate(sa):\n\
    \        rnk[s] = i\n\n    lcp = [0] * (n - 1)\n    h = 0\n    for i in range(n):\n\
    \        if h > 0:\n            h -= 1\n        if rnk[i] == 0:\n            continue\n\
    \n        j = sa[rnk[i] - 1]\n        while j + h < n and i + h < n:\n       \
    \     if S[j + h] != S[i + h]:\n                break\n            h += 1\n  \
    \      lcp[rnk[i] - 1] = h\n\n    return lcp\n"
  dependsOn: []
  isVerificationFile: false
  path: src/string/suffix_array.py
  requiredBy: []
  timestamp: '2023-07-09 20:12:03+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/string/lcp_array.test.py
  - src/$tests/string/suffix_array.test.py
documentation_of: src/string/suffix_array.py
layout: document
redirect_from:
- /library/src/string/suffix_array.py
- /library/src/string/suffix_array.py.html
title: src/string/suffix_array.py
---
