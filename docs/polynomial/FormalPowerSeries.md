---
title: FormalPowerSeries
documentation_of: ././expansion/polynomial/FormalPowerSeries998.py
---

# 概要
FormalPowerSeries です．MOD 998244353 用の者しか作っていません．他の MOD にする場合は適当に変数を変更してください．

list を継承しているので，list に関する演算は割と使います．（オーバーライドしているものを除く）

https://maspypy.com/%E5%A4%9A%E9%A0%85%E5%BC%8F%E3%83%BB%E5%BD%A2%E5%BC%8F%E7%9A%84%E3%81%B9%E3%81%8D%E7%B4%9A%E6%95%B0-%E9%AB%98%E9%80%9F%E3%81%AB%E8%A8%88%E7%AE%97%E3%81%A7%E3%81%8D%E3%82%8B%E3%82%82%E3%81%AE
https://nyaannyaan.github.io/library/fps/formal-power-series.hpp


## 使い方
- \_\_init\_\_(n: int) := 長さ n，初期値 0 のリストで初期化します．
- \_\_init\_\_(A: list[int]) := A で初期化します．A の各要素が [0, MOD) に収まることを仮定しています．
- resize(n) := 長さを n に変更します．
- \_\_add\_\_, \_\_iadd\_\_,  \_\_sub\_\_, \_\_isub\_\_,  \_\_mul\_\_, \_\_imul\_\_, \_\_floordiv\_\_ := FPS における四則演算です
- inv() := $1/f$ を求めます．
- differential() := 微分します
- integral() := 積分します
- log() := $\log{f}$ を求めます
- exp() := $\exp{f}$ を求めます
- pow(k) := $f^n$ を求めます
- sqrt() := $g^2\equiv f$ を満たす$g$を求めます
