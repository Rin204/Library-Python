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
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\n\n\nclass RollingHash:\n    mask30 = (1 << 30) - 1\n    mask31\
    \ = (1 << 31) - 1\n    MOD = (1 << 61) - 1\n    Base = None\n    pw = [1]\n\n\
    \    def __init__(self, S):\n        if RollingHash.Base is None:\n          \
    \  RollingHash.Base = random.randrange(129, 1 << 30)\n        for i in range(len(RollingHash.pw),\
    \ len(S) + 1):\n            RollingHash.pw.append(\n                RollingHash.CalcMod(RollingHash.Mul(RollingHash.pw[i\
    \ - 1], self.__class__.Base))\n            )\n\n        self.hash = [0] * (len(S)\
    \ + 1)\n        for i, s in enumerate(S, 1):\n            self.hash[i] = RollingHash.CalcMod(\n\
    \                RollingHash.Mul(self.hash[i - 1], RollingHash.Base) + ord(s)\n\
    \            )\n\n    def get(self, l, r):\n        return RollingHash.CalcMod(\n\
    \            self.hash[r] - RollingHash.Mul(self.hash[l], RollingHash.pw[r - l])\n\
    \        )\n\n    def Mul(l, r):\n        lu = l >> 31\n        ld = l & RollingHash.mask31\n\
    \        ru = r >> 31\n        rd = r & RollingHash.mask31\n        middlebit\
    \ = ld * ru + lu * rd\n        return (\n            ((lu * ru) << 1)\n      \
    \      + ld * rd\n            + ((middlebit & RollingHash.mask30) << 31)\n   \
    \         + (middlebit >> 30)\n        )\n\n    def CalcMod(val):\n        if\
    \ val < 0:\n            val %= RollingHash.MOD\n        val = (val & RollingHash.MOD)\
    \ + (val >> 61)\n        if val > RollingHash.MOD:\n            val -= RollingHash.MOD\n\
    \        return val\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/string/RollingHash.py
  requiredBy: []
  timestamp: '2023-06-10 17:33:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/string/RollingHash.py
layout: document
redirect_from:
- /library/expansion/string/RollingHash.py
- /library/expansion/string/RollingHash.py.html
title: expansion/string/RollingHash.py
---
