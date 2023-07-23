---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
    links:
    - https://judge.yosupo.jp/problem/aplusb
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    \nfrom src.misc.TopKHeap import TopKHeap\nimport random\n\n\nk = random.randrange(1000,\
    \ 2000)\nA = [random.randrange(10**9) for _ in range(k)]\nhq = TopKHeap(k, False,\
    \ A)\nQ = 1000\nfor _ in range(Q):\n    t = random.randrange(2)\n    if t == 0:\n\
    \        a = random.randrange(10**9)\n        hq.push(a)\n        A.append(a)\n\
    \    else:\n        a = random.choice(A)\n        hq.remove(a)\n        A.remove(a)\n\
    \n    A.sort(reverse=True)\n    assert hq.tot == sum(A[:k])\n\na, b = map(int,\
    \ input().split())\nprint(a + b)\n"
  dependsOn: []
  isVerificationFile: true
  path: src/$tests/misc/TopKHeap.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/misc/TopKHeap.test.py
layout: document
redirect_from:
- /verify/src/$tests/misc/TopKHeap.test.py
- /verify/src/$tests/misc/TopKHeap.test.py.html
title: src/$tests/misc/TopKHeap.test.py
---
