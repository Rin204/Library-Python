# Library-Python

## 注意事項
`***_global_mod` と書かれているものは MOD の値をグローバル変数で宣言しているものです．
基本的に 998244353 にしているので，違う値にしたいときは適宜検索をして使いたい値に変更してください

`src/` と `expansion/` がありますが，コピペして使いたい場合は `expansion/` にあるものを使ってください．
MOD 系は 998244353 を暗に仮定しているものがいくつかあるので，適宜変更してください．

個人用競プロ用で作成したライブラリなので，書き方が変なものは一定すうあると思いますが，ご了承ください．

一部 `Base_` と末尾についている class があります．これらは，主に引数で与える想定になる関数について，
- `Base_` が付いていない場合：引数に与える
- `Base_` が付いている場合：class を継承して各種関数を作成する

使い方を想定しています．使用感は https://github.com/Rin204/Library-Python/blob/main/src/%24tests/data_structure/segtree.test.py https://github.com/Rin204/Library-Python/blob/main/src/%24tests/data_structure/segtree2.test.py あたりを見てください．

## expansion.py

これを使いたい場合，import の際に以下のルールに従ってください
- Python ファイルと同じディレクトリに src/ がそのまま置いてある or src/ へのシンボリックリンクがある
- import の際に `from src.data_structure.UnionFind import *` みたいな記法で import を行っている

現状，`from src.data_structure.UnionFind import aaa, bbb` のようにしても`from src.data_structure.UnionFind import *` にしても元のファイルを全て展開するようになっています（個別の import に対応するのが面倒だったので...）

```
python3 expansion.py A.py exp.py
```
みたいにすると，`A.py` 内の import が全て置き換わった状態で `exp.py` に展開されます

