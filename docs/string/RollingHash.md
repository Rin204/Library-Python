---
title: RollingHash
documentation_of: ././expansion/string/RollingHash.py
---

# 概要
https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
MOD $2^{61} - 1$ のローリングハッシュです．

## 使い方

- \_\_init\_\_(S) := 文字列Sにたいして初期化します．
- get(l, r) := 区間[l, r) の hash 値を取得します．

