---
title: Mo
documentation_of: ././expansion/misc/Mo.py
---

# 概要
Mo algorithm です．
static な数列の区間クエリ Q 個に答えます．

## 使い方
- \_\_init\_\_(ope, n, Q) := 数列の長さとクエリ数を与えて初期化します．（数列自身は与えない想定）
- insert(l, r) := 区間[l, r) に対するクエリを追加します．
- run(add_left, add_right, delete_left, delete_right, rem) := 以下の 5 つの関数を定義して 追加した各クエリの答えを求めます．
    - add_left(l) := 区間を [l, r) から [l - 1, r) にしたときの状態遷移を各関数
    - add_right(l) := 区間を [l, r) から [l, r + 1) にしたときの状態遷移を各関数
    - delete_left(l) := 区間を [l, r) から [l + 1, r) にしたときの状態遷移を各関数
    - delete_right(l) := 区間を [l, r) から [l, r - 1) にしたときの状態遷移を各関数
    - rem(i) := 区間 i の答えを記録する関数
