---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_inversions_query
    links:
    - https://judge.yosupo.jp/problem/static_range_inversions_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query\n\
    from pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.misc.Mo import Mo\nfrom src.data_structure.BIT import BIT\nimport sys\n\
    \ninput = sys.stdin.readline\n\nn, Q = map(int, input().split())\nA = list(map(int,\
    \ input().split()))\ndic = {a: i for i, a in enumerate(sorted(set(A)))}\nA = [dic[a]\
    \ for a in A]\n\nmo = Mo(n, Q)\nfor _ in range(Q):\n    l, r = map(int, input().split())\n\
    \    mo.insert(l, r)\n\nn = len(dic)\nbit = BIT(n)\nans = [0] * Q\ninv = 0\n\n\
    \ndef add_left(i):\n    global inv\n    a = A[i]\n    inv += bit.sum(a)\n    bit.add(a,\
    \ 1)\n\n\ndef add_right(i):\n    global inv\n    a = A[i]\n    inv += bit.sum(a\
    \ + 1, n)\n    bit.add(a, 1)\n\n\ndef delete_left(i):\n    global inv\n    a =\
    \ A[i]\n    inv -= bit.sum(a)\n    bit.add(a, -1)\n\n\ndef delete_right(i):\n\
    \    global inv\n    a = A[i]\n    inv -= bit.sum(a + 1, n)\n    bit.add(a, -1)\n\
    \n\ndef rem(i):\n    ans[i] = inv\n\n\nmo.run(add_left, add_right, delete_left,\
    \ delete_right, rem)\nprint(*ans, sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/misc/Mo.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/misc/Mo.test.py
layout: document
redirect_from:
- /verify/src/$tests/misc/Mo.test.py
- /verify/src/$tests/misc/Mo.test.py.html
title: src/$tests/misc/Mo.test.py
---
