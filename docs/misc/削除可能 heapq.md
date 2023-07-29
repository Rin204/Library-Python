---
title: 削除可能 heapq
documentation_of: ././expansion/misc/DeletableHeapq.py
---

# 概要
削除可能 heapq です．内部で hashDict を使っているので，hack 対策に rnd() を一様に足してあげると良いかもしれません

## 使い方

- \_\_init\_\_(lst=None, reverse=False) := lstに要素を指定すると初期の配列を作ってくれます
reverse=Trueにすると最大値取得に，Falseにすると最小値取得になります．
- \_\_bool\_\_() := 現在の配列長が1以上かどうかを返します．
- \_\_len\_\_() :=現在の配列長を返します．
- top() := heapqの先頭の要素を返します．要素が1つもない場合，`None`を返します．
- \_\_getitem\_\_(i) := hq[0] で top()と同じものをかえします．hq[1]のように，index番号が0で無いケースは対応してません．
- push(x) := heapqにxを追加します．
- pop() := heapqの先頭の要素を削除し，返り値とします．
要素が1つもない場合，`None`を返します．
- remove(x) := heapqからxを削除します．
削除できた場合は`True`を，
削除できなかった場合($x$が存在しなかった場合)は`False`を返します．
