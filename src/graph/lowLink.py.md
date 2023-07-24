---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ''
    path: src/$tests/graph/lowlink_bridges.test.py
    title: src/$tests/graph/lowlink_bridges.test.py
  - icon: ''
    path: src/$tests/graph/lowlinlk_artic.test.py
    title: src/$tests/graph/lowlinlk_artic.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def lowLink(edges):\n    \"\"\"\n    edges[from] = [to1, to2, ...]\n    \"\
    \"\"\n    n = len(edges)\n    ord = [-1] * n\n    low = [-1] * n\n    isartic\
    \ = [False] * n\n    bridge = []\n\n    def dfs(root, k):\n        x = root *\
    \ (n + 1) + n\n        stack = [~x, x]\n        cnt = 0\n        while stack:\n\
    \            tmp = stack.pop()\n            if tmp >= 0:\n                pos\
    \ = tmp // (n + 1)\n                bpos = tmp - (n + 1) * pos\n\n           \
    \     if bpos != n and ord[pos] != -1:\n                    low[bpos] = min(low[bpos],\
    \ ord[pos])\n                    stack.pop()\n                    continue\n\n\
    \                low[pos] = ord[pos] = k\n                k += 1\n           \
    \     for npos in edges[pos]:\n                    if npos == bpos:\n        \
    \                continue\n\n                    if ord[npos] == -1:\n       \
    \                 if bpos == n:\n                            cnt += 1\n      \
    \                  x = npos * (n + 1) + pos\n                        stack.append(~x)\n\
    \                        stack.append(x)\n                    else:\n        \
    \                low[pos] = min(low[pos], ord[npos])\n                       \
    \ if npos == root:\n                            cnt -= 1\n            else:\n\
    \                tmp = ~tmp\n                pos = tmp // (n + 1)\n          \
    \      bpos = tmp - (n + 1) * pos\n\n                if bpos != n and ord[bpos]\
    \ < low[pos]:\n                    bridge.append((min(pos, bpos), max(pos, bpos)))\n\
    \n                if bpos != n and bpos != root and low[pos] >= ord[bpos]:\n \
    \                   isartic[bpos] = True\n\n                if bpos != n:\n  \
    \                  low[bpos] = min(low[bpos], low[pos])\n\n        if cnt >= 2:\n\
    \            isartic[root] = True\n\n        return k\n\n    k = 0\n    for i\
    \ in range(n):\n        if ord[i] == -1:\n            k = dfs(i, k)\n\n    return\
    \ isartic, bridge\n"
  dependsOn: []
  isVerificationFile: false
  path: src/graph/lowLink.py
  requiredBy: []
  timestamp: '2023-07-06 22:57:49+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/graph/lowlinlk_artic.test.py
  - src/$tests/graph/lowlink_bridges.test.py
documentation_of: src/graph/lowLink.py
layout: document
redirect_from:
- /library/src/graph/lowLink.py
- /library/src/graph/lowLink.py.html
title: src/graph/lowLink.py
---