---
title: berlekamp_massey
documentation_of: ././expansion/polynomial/berlekamp_massey.py
---

# 概要
数列$A = [a_0, a_1, ...]$が与えられた時，

$a_i \equiv \sum_{j=1}^d c_j a_{i-j} \pmod {\rm MOD}$を満たす長さ$d$の数列$C$を求めます．$d$は可能な限り最小なものを求めます．

## 使い方
```python
C = berlekamp_massey(A, MOD)
```
