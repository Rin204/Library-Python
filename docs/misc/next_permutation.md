---
title: next_permutation
documentation_of: ././expansion/misc/next_permutation.py
---

# 概要
C++ にある next_permutation を真似して作ったやつです．

## 使い方

### next_permutation(P)
P を与えた際に，P の並び替えのうち，辞書順で P の次に大きいものに変更して True を返します．．存在しない場合，False を返します．破壊的変更を行います．

### prev_permutation(P)
P を与えた際に，P の並び替えのうち，辞書順で P の次に小さいものに変更して True を返します．．存在しない場合，False を返します．破壊的変更を行います．

### all_permutations(P)
```
for Q in all_permutations(P)
```
とすると，P の並び替えのうち，P + P 寄りも辞書順で後ろのものを全て列挙します．Q に変更を加えると P 側にも変更が加わるので注意してください．回る順番は辞書順です．

### rev_all_permutations(P)
`all_permutations` の逆順です．
