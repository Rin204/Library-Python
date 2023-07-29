---
title: 数列を上位k個を管理するやつ
documentation_of: ././expansion/misc/TopKHeap.py
---

# 概要
数列の（最大）上位 K 個を管理しておく用のやつです．内部で hashDict を使っているので，hack 対策に rnd() を一様に足してあげると良いかもしれません

## 使い方

- \_\_init\_\_(K, reverse=False, A=None) := reverse=True にすると大きいほうから，False にすると小さいほうから K 個を管理します．Aに要素を指定すると初期の配列を作ってくれます
- \_\_len\_\_() :=現在の配列長を返します．
- tot := 上位 K 個の合計を返します．
- sum := 上位 K 個の合計を返します．(tot と同じ)
- push(x) := xを追加します．
- remove(x) := xを削除します．存在しない場合未定義です
