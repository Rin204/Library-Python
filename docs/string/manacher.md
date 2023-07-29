---
title: manacher
documentation_of: ././expansion/string/manacher.py
---

# 概要
manacher です．

(0-indexed で) 返り値の 2i 番目の値は i 番目の文字を中心とする回文の最大長を，2i + 1 番目の値は i 番目の文字と i + 1 番目の文字の区切れ目を中心とする回文の最大長です．

## 使い方

```python
res = manacher(S)
```
