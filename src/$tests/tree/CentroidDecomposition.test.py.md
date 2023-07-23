---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/BIT.py
    title: src/data_structure/BIT.py
  - icon: ':x:'
    path: src/tree/CentroidDecomposition.py
    title: src/tree/CentroidDecomposition.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/1038
    links:
    - https://yukicoder.me/problems/no/1038
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/1038\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \n## yukicoder \u306E\u30AA\u30F3\u30E9\u30A4\u30F3\u5B9F\u884C\u3060\u3068TL\u306B\
    \u9593\u306B\u5408\u3063\u305F\u308A\u9593\u306B\u5408\u308F\u306A\u304B\u3063\
    \u305F\u308A\u3059\u308B\n\nfrom src.tree.CentroidDecomposition import CentroidDecomposition\n\
    from src.data_structure.BIT import BIT\nimport sys\n\ninput = sys.stdin.readline\n\
    \n\nn, Q = map(int, input().split())\nG = CentroidDecomposition(n)\nG.read_edges()\n\
    G.build()\nlogn = len(G.centroids)\nbit = []\nsubbit = []\nL = [0] * n\nsubL =\
    \ [0] * n\n\nfor d in range(logn):\n    c = 0\n    c2 = 0\n    for g in G.centroids[d]:\n\
    \        L[g] = c\n        if d != 0:\n            subL[g] = c2\n        c +=\
    \ G.size[g]\n        c2 += G.size[g] + 1\n    bit.append(BIT(c))\n    if d !=\
    \ 0:\n        subbit.append(BIT(c2))\n\n\ndef add(x, y, z):\n    bg = -1\n   \
    \ for g, d in G.cent_ind_dist(x):\n        dd = y - d\n        if dd >= 0:\n \
    \           bit[G.depth[g]].add(L[g], z)\n            bit[G.depth[g]].add(L[g]\
    \ + min(dd + 1, G.size[g]), -z)\n            if bg != -1:\n                subbit[G.depth[g]].add(subL[bg]\
    \ + 1, z)\n                subbit[G.depth[g]].add(subL[bg] + min(dd + 1, G.size[bg]\
    \ + 1), -z)\n        bg = g\n\n\ndef get(x):\n    bg = -1\n    ret = 0\n    for\
    \ g, d in G.cent_ind_dist(x):\n        ret += bit[G.depth[g]].sum(L[g] + d + 1)\n\
    \        if bg != -1:\n            ret -= subbit[G.depth[g]].sum(subL[bg] + d\
    \ + 1)\n        bg = g\n\n    return ret\n\n\nout = []\nfor _ in range(Q):\n \
    \   x, y, z = map(int, input().split())\n    x -= 1\n    out.append(get(x))\n\
    \    add(x, y, z)\n\nprint(*out, sep=\"\\n\")\n"
  dependsOn:
  - src/tree/CentroidDecomposition.py
  - src/data_structure/BIT.py
  isVerificationFile: true
  path: src/$tests/tree/CentroidDecomposition.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/tree/CentroidDecomposition.test.py
layout: document
redirect_from:
- /verify/src/$tests/tree/CentroidDecomposition.test.py
- /verify/src/$tests/tree/CentroidDecomposition.test.py.html
title: src/$tests/tree/CentroidDecomposition.test.py
---
