---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def partial_match_table(word):\n    n = len(word)\n    table = [0] * (n +\
    \ 1)\n    table[0] = -1\n\n    i = 0\n    j = 1\n    while j < n:\n        matched\
    \ = word[i] == word[j]\n        if not matched and i > 0:\n            i = table[i]\n\
    \        else:\n            if matched:\n                i += 1\n            j\
    \ += 1\n            table[j] = i\n\n    return table\n\n\ndef kmp_search(text,\
    \ word):\n    table = partial_match_table(word)\n    n = len(text)\n\n    i =\
    \ p = 0\n    ret = []\n    while i < n:\n        if text[i] == word[p]:\n    \
    \        i += 1\n            p += 1\n            if p == len(word):\n        \
    \        ret.append(i - p)\n                p = table[p]\n        else:\n    \
    \        p = table[p]\n            if p < 0:\n                i += 1\n       \
    \         p += 1\n\n    return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/string/KMP.py
  requiredBy: []
  timestamp: '2023-06-18 16:02:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/string/KMP.py
layout: document
redirect_from:
- /library/expansion/string/KMP.py
- /library/expansion/string/KMP.py.html
title: expansion/string/KMP.py
---
