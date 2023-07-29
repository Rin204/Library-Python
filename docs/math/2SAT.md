---
title: 2SAT
documentation_of: ././expansion/math/TwoSAT.py
---

# 概要
2SAT です．

## 使い方

- \_\_init\_\_(n) := 変数の個数を n で初期化します．
- add_clause(i, pos_i, j, pos_j) := $(x_i == pos_i) \cup (x_j == pos_j)$ の条件を追加します．
- check() := 2SAT が充足可能かを判定します．
- assign() := 充足可能である場合，有効な割り当ての１つを返します．充足不
可能な場合は未定義です．
