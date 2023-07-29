---
title: AhoCorasick
documentation_of: ././expansion/string/AhoCorasick.py
---

# 概要
AhoCorasick です．

## 使い方
- \_\_init\_\_(words=None) := words を指定すると，それをあらかじめ登録してくれます．
- register(word) := word を登録します
- build() := 与えられた word を用いて王地区します．
- search(text) := 以下の2次元配列の形式で登録した word と match する箇所を返します．
  - matched[i] := $[j_1, j_2, \ldots]$ ($j_1, j_2, \ldots$ はtext$[i:i+|word_j|] = words[j]$ であるもの全て)
