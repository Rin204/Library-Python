---
title: SegmentTreeBase_
documentation_of: ././expansion/data_structure/SegmentTreeBase_.py
---

# 概要
SegmentTree と演算の定義方法以外同じです．

## 使い方
```Python
class PointAddRangeSum(SegmentTreeBase_):
    def ope(self, l, r):
        return l + r

    def e(self):
        return 0
```
みたいにして `ope`, `e` を定義して，`__init__()` には上記2つを与えないようにしてください．
あとは同じです．
