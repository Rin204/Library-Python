---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: src/data_structure/BIT.py
    title: src/data_structure/BIT.py
  - icon: ':x:'
    path: src/misc/DeletableHeapq.py
    title: src/misc/DeletableHeapq.py
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
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\nfrom\
    \ pathlib import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from src.data_structure.BIT import BIT\nfrom src.misc.DeletableHeapq import DeletableHeapq\n\
    import random\n\nrandom.seed(10)\n\nn = 500000\nt = 500000\nA = random.choices(range(n),\
    \ k=t + 10)\ncnt = len(A)\ntot = sum(A)\nif random.random() > 0.5:\n    hq = DeletableHeapq(A)\n\
    else:\n    hq = DeletableHeapq(A, reverse=True)\nbit = BIT(n)\nfor a in A:\n \
    \   bit.add(a, 1)\n\nfor _ in range(t):\n    if random.random() < 0.3:\n     \
    \   p = hq[0]\n        assert bit.get(p) >= 1\n        if hq.pm == 1:\n      \
    \      assert bit.lower_bound(1) - 1 == p\n        else:\n            assert bit.lower_bound(cnt)\
    \ - 1 == p\n        bit.add(p, -1)\n        assert p == hq.pop()\n        cnt\
    \ -= 1\n        tot -= p\n    else:\n        p = random.randrange(n)\n       \
    \ if bit.get(p) == 0 or random.random() < 0.5:\n            bit.add(p, 1)\n  \
    \          hq.push(p)\n            cnt += 1\n            tot += p\n        else:\n\
    \            bit.add(p, -1)\n            assert hq.remove(p)\n            cnt\
    \ -= 1\n            tot -= p\n\n    assert len(hq) == cnt\n    assert hq.tot ==\
    \ tot, (_, hq.tot, tot)\n\n\na, b = map(int, input().split())\nprint(a + b)\n"
  dependsOn:
  - src/misc/DeletableHeapq.py
  - src/data_structure/BIT.py
  isVerificationFile: true
  path: src/$tests/misc/DeletableHeapq.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: src/$tests/misc/DeletableHeapq.test.py
layout: document
redirect_from:
- /verify/src/$tests/misc/DeletableHeapq.test.py
- /verify/src/$tests/misc/DeletableHeapq.test.py.html
title: src/$tests/misc/DeletableHeapq.test.py
---
