---
title: bitwise or convolution
documentation_of: ././expansion/convolution/or_convolution.py
---

# 概要
数列 A, B が与えられたときに
$C_k = \sum_{k = i| j} A_i B_j$
となる C を指定した MOD で割ったあまりを求めます．`MOD=-1`の場合は余りを取らずにそのまま返します．

## 使い方

```
C = or_convolution(A, B, MOD)
```
