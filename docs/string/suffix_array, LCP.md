---
title: suffix_array, LCP
documentation_of: ././expansion/string/suffix_array.py
---

# 概要
suffix_array と LCP です．

$NAIVE_THR$, $DOUBLING_THR$ は愚直でやるかダブリングでやるか sa-is でやるかの閾値です．
## 使い方

```python
sa = suffix_array(S, NAIVE_THR=10, DOUBLING_THR=40)

lcp = lcp_array(S, sa)
```
