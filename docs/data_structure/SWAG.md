---
title: SWAG
documentation_of: ././expansion/data_structure/SWAG.py
---

# 概要
deque に対して要素の追加 / 削除 / 現在の列に対する演算結果取得 を処理します．

演算については
- $f(a, f(b, c)) = f(f(a, b), c)$
- 単位元が存在する

ものを想定しています．（本当は単位元はいらないはずなんですが，実装の都合上要求しているので，ない場合は適当に取りえない値を設定して演算の中で if 文を入れてください）


## 使い方
- \_\_init\_\_(ope, e) := 扱う演算を定義します
- push(x) := deque の末尾に x を追加します．
- pop(x) := deque の先頭の要素を削除します．
- prod() := 現在の deque 列に対する演算結果を返します
- size() := deque 列の長さを返します．
- \_\_len\_\_ := 上記同様
- clear() := deque を空にします．
