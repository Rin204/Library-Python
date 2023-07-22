---
title: bitwise xor convolution
documentation_of: ././expansion/convolution/xor_convolution.py
---

# 概要
数列 A, B が与えられたときに
$C_k = \sum_{k = i \oplus j} A_i B_j$
となる C を指定した MOD で割ったあまりを求めます．($\oplus$ は bitwise xor) `MOD=-1`の場合は余りを取らずにそのまま返します．

## 使い方

```
C = xor_convolution(A, B, MOD)
```
