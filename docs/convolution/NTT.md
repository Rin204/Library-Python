---
title: NTT
documentation_of: ././expansion/convolution/NTT.py
---

# 概要
畳み込みです．MOD = 998244353 の場合は[専用のもの](https://github.com/Rin204/Library-Python/blob/main/src/convolution/NTT998.py)を作成しているので，そちらを使ってください．

## 使い方

- \_\_init\_\_(self, MOD) := 畳み込みに用いる MOD を指定します．
- multiply(A, B) := A と B を畳み込んだ結果を返します．
