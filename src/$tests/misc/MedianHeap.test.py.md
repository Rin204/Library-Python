---
data:
  _extendedDependsOn:
  - icon: ''
    path: src/misc/MadianHeap.py
    title: src/misc/MadianHeap.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.misc.MadianHeap import MedianHeap\nimport random\n\n\nA = [random.randrange(10**9)\
    \ for _ in range(2000)]\nhq = MedianHeap(A)\nQ = 1000\nfor _ in range(Q):\n  \
    \  t = random.randrange(2)\n    if t == 0:\n        a = random.randrange(10**9)\n\
    \        hq.push(a)\n        A.append(a)\n    else:\n        a = random.choice(A)\n\
    \        hq.remove(a)\n        A.remove(a)\n\n    A.sort()\n    n = len(A)\n \
    \   if n % 2 == 1:\n        assert hq.get_med() == [A[n // 2], A[n // 2]]\n  \
    \  else:\n        assert hq.get_med() == [A[n // 2 - 1], A[n // 2]]\n\n    m =\
    \ A[n // 2]\n    assert hq.abs_sum() == sum(abs(a - m) for a in A)\n\n\na, b =\
    \ map(int, input().split())\nprint(a + b)\n"
  dependsOn:
  - src/misc/MadianHeap.py
  isVerificationFile: true
  path: src/$tests/misc/MedianHeap.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/misc/MedianHeap.test.py
layout: document
redirect_from:
- /verify/src/$tests/misc/MedianHeap.test.py
- /verify/src/$tests/misc/MedianHeap.test.py.html
title: src/$tests/misc/MedianHeap.test.py
---
