---
title: wildcard_matching
documentation_of: ././expansion/string/wildcard_matching.py
---

# 概要
文字列のワイルドカード付マッチングです．

MOD 998 の畳み込みを用いているので，非常に低い確率で落ちます．

## 使い方

```python
res = wildcard_matching(S, T, wild="?")
```
res[i] = True のとき，$S[i:i+|T|] = T$ です．
