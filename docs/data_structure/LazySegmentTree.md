---
title: LazySegmentTree
documentation_of: ././expansion/data_structure/LazySegmentTree.py
---

# 概要
主に 区間更新と区間に対する演算に高速に答えるためのデータ構造です．_Base がついている方の使用法に関しては，SegmentTree の方と基本的に同様です

## 使い方
- \_\_init\_\_(n, ope, e, mapping, composition, id_ init=None) := 長さ $n$ の配列 A を作成します．各変数については ac-library のものと同様のものを想定しているので，それを参考にしてください．`init=None`に長さ$n$の配列を指定した場合はそれが初期値に，そうでない場合は `e` が初期値になります．
- set(i, x) := i 番目の値を x に変更します．
- get(i) := A[i] の値を求めます．
- \_\_getitem\_\_(i) := `get(i)` と同じ
- \_\_setitem\_\_(i) := `set(i, x)` と同じ
- prod(l, r) := 区間 $[l, r)$ の演算結果を返します．
- apply(l, r, f) := 区間 $[l, r)$ を．mapping で指定した更新ルールで更新します
- apply(x, f) := 区間 $[x, x + 1)$ を．mapping で指定した更新ルールで更新します
- max_right(self, l, f) := 関数 f を与えて segtree 上で二分探索をします．ac-library にあるものと同じ仕様です．
- max_left(self, r, f) := 関数 f を与えて segtree 上で二分探索をします．ac-library にあるものと同じ仕様です．
