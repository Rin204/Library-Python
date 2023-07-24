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
  code: "def next_permutation(P):\n    n = len(P)\n    for i in range(n - 2, -1, -1):\n\
    \        if P[i] < P[i + 1]:\n            l = i + 1\n            r = n - 1\n \
    \           while r > l:\n                P[l], P[r] = P[r], P[l]\n          \
    \      l += 1\n                r -= 1\n            for j in range(i + 1, n):\n\
    \                if P[i] < P[j]:\n                    P[i], P[j] = P[j], P[i]\n\
    \                    return True\n    return False\n\n\ndef all_permutations(P):\n\
    \    # \u5168\u5217\u6319\u3057\u305F\u3044\u5834\u5408\u306F\u30BD\u30FC\u30C8\
    \u3057\u3066\u3042\u308B\u72B6\u614B\u3067\u6E21\u3059\n    yield P\n    while\
    \ next_permutation(P):\n        yield P\n\n\ndef prev_permutation(P):\n    n =\
    \ len(P)\n    for i in range(n - 2, -1, -1):\n        if P[i] > P[i + 1]:\n  \
    \          l = i + 1\n            r = n - 1\n            while r > l:\n      \
    \          P[l], P[r] = P[r], P[l]\n                l += 1\n                r\
    \ -= 1\n            for j in range(i + 1, n):\n                if P[i] > P[j]:\n\
    \                    P[i], P[j] = P[j], P[i]\n                    return True\n\
    \    return False\n\n\ndef rev_all_permutations(P):\n    # \u5168\u5217\u6319\u3057\
    \u305F\u3044\u5834\u5408\u306F\u9006\u9806\u30BD\u30FC\u30C8\u3057\u3066\u3042\
    \u308B\u72B6\u614B\u3067\u6E21\u3059\n    yield P\n    while prev_permutation(P):\n\
    \        yield P\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/misc/next_permutation.py
  requiredBy: []
  timestamp: '2023-06-18 15:21:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/misc/next_permutation.py
layout: document
redirect_from:
- /library/expansion/misc/next_permutation.py
- /library/expansion/misc/next_permutation.py.html
title: expansion/misc/next_permutation.py
---
