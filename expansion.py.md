---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import os\nimport sys\n\n\ndef main(input_file, output_file):\n    with open(output_file,\
    \ \"w\") as f:\n        se = set()\n\n        def dfs(path):\n            filename\
    \ = \"/\".join(path)\n            if not os.path.exists(filename):\n         \
    \       return False\n            if filename in se:\n                return True\n\
    \            se.add(filename)\n            path.pop()\n            with open(filename,\
    \ \"r\") as f2:\n                for row in f2:\n                    if row[:4]\
    \ == \"from\":\n                        P = row.split()[1].split(\".\")\n    \
    \                    P[-1] += \".py\"\n                        if not dfs(P):\n\
    \                            f.write(row)\n                    else:\n       \
    \                 f.write(row)\n            return True\n\n        path = input_file.split(\"\
    /\")\n        dfs(path)\n\n\nif __name__ == \"__main__\":\n    input_file = sys.argv[1]\n\
    \    output_file = sys.argv[2]\n    main(input_file, output_file)\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion.py
layout: document
redirect_from:
- /library/expansion.py
- /library/expansion.py.html
title: expansion.py
---
