# Library-Python

https://rin204.github.io/Library-Python/

## 注意事項
`***_global_mod` と書かれているものは MOD の値をグローバル変数で宣言しているものです．
基本的に 998244353 にしているので，違う値にしたいときは適宜検索をして使いたい値に変更してください

`***_Base` と書かれている / 書かれていないだけの差分があるものがあります．基本的にクラスを扱うのに関数を与えなければいけないもので，書かれていない場合は引数に与える，書かれている場合はクラスを継承して関数を定義することを想定しています．

`src/` と `expansion/` がありますが，コピペして使いたい場合は `expansion/` にあるものを使ってください．
MOD 系は 998244353 を暗に仮定しているものがいくつかあるので，適宜変更してください．

個人用競プロ用で作成したライブラリなので，書き方が変なものは一定数あると思いますが，ご了承ください (& バグがあったらごめんなさい)．

作成者が数学に明るくない人間なので，いくつか誤用等があると思います．ご了承ください．


## expansion.py

これを使いたい場合，import の際に以下のルールに従ってください
- Python ファイルと同じディレクトリに src/ がそのまま置いてある or src/ へのシンボリックリンクがある
- import の際に `from src.data_structure.UnionFind import *` みたいな記法で import を行っている

現状，`from src.data_structure.UnionFind import aaa, bbb` のようにしても`from src.data_structure.UnionFind import *` にしても元のファイルを全て展開するようになっています（個別の import に対応するのが面倒だったので...）

```
python3 expansion.py A.py exp.py
```
みたいにすると，`A.py` 内の import が全て置き換わった状態で `exp.py` に展開されます

