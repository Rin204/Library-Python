---
title: ConvexHullTrick
documentation_of: ././expansion/data_structure/ConvexHullTrick.py
---

# 概要
以下のクエリを処理します

- 1 次関数 $f(x) = ax + b$ を追加
- 追加された 1 次関数のうち ある x において最小値を取るもの（の $f(x)$ の値）を返す

ただし，
- 追加する 1 時間数の傾きが単調減少である
- 最小値クエリの x の値が単調増加である

必要があります．増加 / 減少を逆にしたい場合は適当に -1 をかけて調整してください



## 使い方
- \_\_init\_\_() := 
- add_line(a, b) := $f(x) = ax + b$ を追加します．
- get(x) := x における最小値を返します
