---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: src/$tests/string/RollingHash.test.py
    title: src/$tests/string/RollingHash.test.py
  - icon: ':x:'
    path: src/$tests/string/wildcard_mathing.test.py
    title: src/$tests/string/wildcard_mathing.test.py
  _isVerificationFailed: true
  _pathExtension: py
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\r\n\r\n\r\nclass RollingHash:\r\n    mask30 = (1 << 30) - 1\r\
    \n    mask31 = (1 << 31) - 1\r\n    MOD = (1 << 61) - 1\r\n    Base = None\r\n\
    \    pw = [1]\r\n\r\n    def __init__(self, S):\r\n        if RollingHash.Base\
    \ is None:\r\n            RollingHash.Base = random.randrange(129, 1 << 30)\r\n\
    \        for i in range(len(RollingHash.pw), len(S) + 1):\r\n            RollingHash.pw.append(\r\
    \n                RollingHash.CalcMod(RollingHash.Mul(RollingHash.pw[i - 1], self.__class__.Base))\r\
    \n            )\r\n\r\n        self.hash = [0] * (len(S) + 1)\r\n        for i,\
    \ s in enumerate(S, 1):\r\n            self.hash[i] = RollingHash.CalcMod(\r\n\
    \                RollingHash.Mul(self.hash[i - 1], RollingHash.Base) + ord(s)\r\
    \n            )\r\n\r\n    def get(self, l, r):\r\n        return RollingHash.CalcMod(\r\
    \n            self.hash[r] - RollingHash.Mul(self.hash[l], RollingHash.pw[r -\
    \ l])\r\n        )\r\n\r\n    def Mul(l, r):\r\n        lu = l >> 31\r\n     \
    \   ld = l & RollingHash.mask31\r\n        ru = r >> 31\r\n        rd = r & RollingHash.mask31\r\
    \n        middlebit = ld * ru + lu * rd\r\n        return (\r\n            ((lu\
    \ * ru) << 1)\r\n            + ld * rd\r\n            + ((middlebit & RollingHash.mask30)\
    \ << 31)\r\n            + (middlebit >> 30)\r\n        )\r\n\r\n    def CalcMod(val):\r\
    \n        if val < 0:\r\n            val %= RollingHash.MOD\r\n        val = (val\
    \ & RollingHash.MOD) + (val >> 61)\r\n        if val > RollingHash.MOD:\r\n  \
    \          val -= RollingHash.MOD\r\n        return val\r\n"
  dependsOn: []
  isVerificationFile: false
  path: src/string/RollingHash.py
  requiredBy: []
  timestamp: '2023-06-12 00:17:20+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - src/$tests/string/wildcard_mathing.test.py
  - src/$tests/string/RollingHash.test.py
documentation_of: src/string/RollingHash.py
layout: document
redirect_from:
- /library/src/string/RollingHash.py
- /library/src/string/RollingHash.py.html
title: src/string/RollingHash.py
---
