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
  code: "import os\nimport datetime\nimport glob\nimport json\n\n\ndef get_time_expfile(input_file):\n\
    \    write = []\n    se = set()\n\n    def dfs(path):\n        filename = \"/\"\
    .join(path)\n        if not os.path.exists(filename):\n            return False\n\
    \        if filename in se:\n            return True\n        se.add(filename)\n\
    \        path.pop()\n        with open(filename, \"r\") as f2:\n            for\
    \ row in f2:\n                if row[:4] == \"from\":\n                    P =\
    \ row.split()[1].split(\".\")\n                    P[-1] += \".py\"\n        \
    \            if not dfs(P):\n                        write.append(row)\n     \
    \           else:\n                    write.append(row)\n        return True\n\
    \n    path = input_file.split(\"/\")\n    dfs(path)\n\n    max_time = max(datetime.datetime.fromtimestamp(os.path.getmtime(file))\
    \ for file in se)\n    return max_time, \"\".join(write)\n\n\ndef main():\n  \
    \  json_path = \"src/timestamps.json\"\n    timestamps = {}\n    if os.path.exists(json_path):\n\
    \        with open(json_path) as fh:\n            data = json.load(fh)\n     \
    \   for path, timestamp in data.items():\n            if path == \"~\" and timestamp\
    \ == \"dummy\":  # for backward compatibility\n                continue\n    \
    \        timestamps[path] = timestamp\n    data = {}\n    for file in glob.glob(\"\
    src/**/*.py\", recursive=True):\n        time, write = get_time_expfile(file)\n\
    \        data[file] = time.strftime(\"%Y-%m-%d %H:%M:%S\")\n        if timestamps.get(file,\
    \ None) == data[file]:\n            continue\n        output_file = file.replace(\"\
    src\", \"expansion\", 1)\n        with open(output_file, \"w\") as f:\n      \
    \      f.write(write)\n        print(f\"copy {file}\")\n\n    with open(json_path,\
    \ \"w\") as fh:\n        json.dump(data, fh, sort_keys=True, indent=0)\n\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion_all.py
  requiredBy: []
  timestamp: '2023-07-22 23:47:53+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion_all.py
layout: document
redirect_from:
- /library/expansion_all.py
- /library/expansion_all.py.html
title: expansion_all.py
---
