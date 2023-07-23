---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/1013
    links:
    - https://yukicoder.me/problems/1013
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/1013\nfrom pathlib\
    \ import Path\nimport sys\n\nsys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))\n\
    from collections import deque\n\n\nclass AhoCorasick:\n    def __init__(self,\
    \ words=None):\n        if words is None:\n            self.words = []\n     \
    \   else:\n            self.words = words\n\n    def register(self, word):\n \
    \       self.words.append(word)\n\n    def build(self):\n        self.children\
    \ = [{}]\n        self.match = [[]]\n\n        for i, word in enumerate(self.words):\n\
    \            self._register(i, word)\n\n        self.failure = [0] * len(self.children)\n\
    \        self._create_failure()\n\n    def _register(self, i, word):\n       \
    \ k = 0\n        for s in word:\n            if s in self.children[k]:\n     \
    \           k = self.children[k][s]\n            else:\n                le = len(self.children)\n\
    \                self.children[k][s] = le\n                self.children.append({})\n\
    \                self.match.append([])\n                k = le\n\n        self.match[k].append(i)\n\
    \n    def _create_failure(self):\n        queue = deque(self.children[0].values())\n\
    \        while queue:\n            k = queue.popleft()\n            b = self.failure[k]\n\
    \            for s, j in self.children[k].items():\n                self.failure[j]\
    \ = self._next(b, s)\n                self.match[j] += self.match[self.failure[j]]\n\
    \                queue.append(j)\n\n    def _next(self, k, s):\n        while\
    \ 1:\n            if s in self.children[k]:\n                return self.children[k][s]\n\
    \            elif k == 0:\n                return 0\n\n            k = self.failure[k]\n\
    \n    def search(self, text):\n        k = 0\n        le = len(text)\n       \
    \ matched = [[] for _ in range(le)]\n        for i, s in enumerate(text):\n  \
    \          k = self._next(k, s)\n            for m in self.match[k]:\n       \
    \         matched[i - len(self.words[m]) + 1].append(m)\n\n        return matched\n\
    \n\nS = input()\nn = int(input())\nac = AhoCorasick()\nfor i in range(n):\n  \
    \  T = input()\n    ac.register(T)\n\nac.build()\nmatch = ac.search(S)\nls = len(S)\n\
    ans = 0\nfor row in match:\n    ans += len(row)\n\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: expansion/$tests/string/AhoCorasick.test.py
  requiredBy: []
  timestamp: '2023-07-23 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: expansion/$tests/string/AhoCorasick.test.py
layout: document
redirect_from:
- /verify/expansion/$tests/string/AhoCorasick.test.py
- /verify/expansion/$tests/string/AhoCorasick.test.py.html
title: expansion/$tests/string/AhoCorasick.test.py
---
