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
    , line 81, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \                   ^^^^^^^^^^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 108, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\n\n\nclass DeletableHeapq:\n    def __init__(self, lst=None,\
    \ reverse=False):\n        if reverse:\n            self.pm = -1\n        else:\n\
    \            self.pm = 1\n        if lst is None:\n            self.hq = []\n\
    \        else:\n            self.hq = [self.pm * x for x in lst]\n\n        heapq.heapify(self.hq)\n\
    \        self.tot = sum(self.hq) * self.pm\n        self.cnt = {}\n        for\
    \ x in self.hq:\n            self.cnt[x] = self.cnt.get(x, 0) + 1\n        self.length\
    \ = len(self.hq)\n\n    def __bool__(self):\n        return bool(self.hq)\n\n\
    \    def __len__(self):\n        return self.length\n\n    @property\n    def\
    \ sum(self):\n        return self.tot\n\n    def top(self):\n        if self.hq:\n\
    \            return self.hq[0] * self.pm\n        else:\n            return None\n\
    \n    def __getitem__(self, i):\n        # \u5148\u982D\u8981\u7D20\u306B\u30A2\
    \u30AF\u30BB\u30B9\u3057\u305F\u3044\u3068\u304D\u306E\u307F\n        assert i\
    \ == 0\n        return self.top()\n\n    def push(self, x):\n        self.length\
    \ += 1\n        self.cnt[x * self.pm] = self.cnt.get(x * self.pm, 0) + 1\n   \
    \     self.tot += x\n        heapq.heappush(self.hq, x * self.pm)\n\n    def pop(self):\n\
    \        if not self.hq:\n            return None\n        self.length -= 1\n\
    \        x = heapq.heappop(self.hq)\n        self.cnt[x] -= 1\n        self.tot\
    \ -= x * self.pm\n        self._delete()\n        return x * self.pm\n\n    def\
    \ remove(self, x):\n        if self.cnt.get(x * self.pm, 0) == 0:\n          \
    \  return False\n        self.length -= 1\n        self.cnt[x * self.pm] -= 1\n\
    \        self.tot -= x\n        self._delete()\n        return True\n\n    def\
    \ _delete(self):\n        while self.hq and self.cnt.get(self.hq[0], 0) == 0:\n\
    \            heapq.heappop(self.hq)\n"
  dependsOn: []
  isVerificationFile: false
  path: expansion/misc/DeletableHeapq.py
  requiredBy: []
  timestamp: '2023-06-22 23:45:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: expansion/misc/DeletableHeapq.py
layout: document
title: "\u524A\u9664\u53EF\u80FD heapq"
---

# 概要
削除可能 heapq です．内部で hashDict を使っているので，hack 対策に rnd() を一様に足してあげると良いかもしれません

## 使い方

- \_\_init\_\_(lst=None, reverse=False) := lstに要素を指定すると初期の配列を作ってくれます
reverse=Trueにすると最大値取得に，Falseにすると最小値取得になります．
- \_\_bool\_\_() := 現在の配列長が1以上かどうかを返します．
- \_\_len\_\_() :=現在の配列長を返します．
- top() := heapqの先頭の要素を返します．要素が1つもない場合，`None`を返します．
- \_\_getitem\_\_(i) := hq[0] で top()と同じものをかえします．hq[1]のように，index番号が0で無いケースは対応してません．
- push(x) := heapqにxを追加します．
- pop() := heapqの先頭の要素を削除し，返り値とします．
要素が1つもない場合，`None`を返します．
- remove(x) := heapqからxを削除します．
削除できた場合は`True`を，
削除できなかった場合($x$が存在しなかった場合)は`False`を返します．
