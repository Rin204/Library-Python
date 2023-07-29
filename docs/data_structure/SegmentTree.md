---
title: SegmentTree
documentation_of: ././expansion/data_structure/SegmentTree.py
---

# 概要
主に 1 点更新と区間に対する演算に高速に答えるためのデータ構造です．

## 使い方
- \_\_init\_\_(n, ope, e, init=None) := 長さ $n$ の配列 A を作成します．`ope` が指定する演算で，`e` が単位元です．`init=None`に長さ$n$の配列を指定した場合はそれが初期値に，そうでない場合は `e` が初期値になります．
- build() := セグメント木の各値を全て再計算します．（あまり用途はないですが，O(N) 個所を直接変更した後まとめて計算したい場合等）
- set(i, x) := i 番目の値を x に変更します．
- get(i) := A[i] の値を求めます．
- \_\_getitem\_\_(i) := `get(i)` と同じ
- \_\_setitem\_\_(i) := `set(i, x)` と同じ
- prod(l, r) := 区間 $[l, r)$ の演算結果を返します．
- max_right(self, l, f) := 関数 f を与えて segtree 上で二分探索をします．[ac-library](https://atcoder.github.io/ac-library/master/document_ja/segtree.html) にあるものと同じ仕様です．
- max_left(self, r, f) := 関数 f を与えて segtree 上で二分探索をします．[ac-library](https://atcoder.github.io/ac-library/master/document_ja/segtree.html) にあるものと同じ仕様です．
