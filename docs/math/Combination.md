---
title: Combination
documentation_of: ././expansion/math/Combination.py
---

# 概要
素数 MOD の二項係数関連を求めます

## 使い方

- \_\_init\_\_(n, MOD=998244353) := n の上限を指定します．（範囲外参照をしそうになると勝手に拡張してくれますが（fact, invfact を直接見る場合を除く），初めから十分な範囲を確保しておいた方が安心です．）
- nPk(n, k) := nPk(n, k) を求めます
- nCk(n, k) := nCk(n, k) を求めます
- nHk(n, k) := nHk(n, k) を求めます
- Catalan(n) := カタラン数を求めます．
