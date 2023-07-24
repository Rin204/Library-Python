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
  code: "import os\nimport sys\nfrom io import BytesIO, IOBase\n\nBUFSIZE = 8192\n\
    \n\nclass FastIO(IOBase):\n    newlines = 0\n\n    def __init__(self, file):\n\
    \        self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        while True:\n   \
    \         b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n  \
    \          if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        while self.newlines == 0:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            self.newlines = b.count(b\"\\n\") + (not b)\n       \
    \     ptr = self.buffer.tell()\n            self.buffer.seek(0, 2), self.buffer.write(b),\
    \ self.buffer.seek(ptr)\n        self.newlines -= 1\n        return self.buffer.readline()\n\
    \n    def flush(self):\n        if self.writable:\n            os.write(self._fd,\
    \ self.buffer.getvalue())\n            self.buffer.truncate(0), self.buffer.seek(0)\n\
    \n\nclass IOWrapper(IOBase):\n    def __init__(self, file):\n        self.buffer\
    \ = FastIO(file)\n        self.flush = self.buffer.flush\n        self.writable\
    \ = self.buffer.writable\n        self.write = lambda s: self.buffer.write(s.encode(\"\
    ascii\"))\n        self.read = lambda: self.buffer.read().decode(\"ascii\")\n\
    \        self.readline = lambda: self.buffer.readline().decode(\"ascii\")\n\n\n\
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)\n\n\ndef input():\n\
    \    return sys.stdin.readline().rstrip(\"\\r\\n\")\n"
  dependsOn: []
  isVerificationFile: false
  path: src/misc/FastIO.py
  requiredBy: []
  timestamp: '2023-06-10 17:32:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: src/misc/FastIO.py
layout: document
redirect_from:
- /library/src/misc/FastIO.py
- /library/src/misc/FastIO.py.html
title: src/misc/FastIO.py
---
