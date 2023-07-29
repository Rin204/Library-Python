---
title: CombinationArbitrary
documentation_of: ././expansion/math/CombinationArbitrary.py
---

# 概要
任意 MOD の二項係数を求めます

## 使い方

- \_\_init\_\_(MOD, n=-1) := n の上限を指定します．MOD を素因数分解した結果の 各 $P_i ^ {e_i}$ について，$P_i ^ {e_i} \le n$ の場合，上限関係なくすべての値を求められます (-1 の場合これ)
- nCk(n, k) := nCk(n, k) を求めます
