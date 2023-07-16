# Library-Python

## 注意事項
`***_global_mod` と書かれているものは MOD の値をグローバル変数で宣言しているものです．
基本的に 998244353 にしているので，違う値にしたいときは適宜検索をして使いたい値に変更してください


## expansion

これを使いたい場合，import の際に以下のルールに従ってください
- Python ファイルと同じディレクトリに src/ がそのまま置いてある or src/ へのシンボリックリンクがある
- import の際に `from src.data_structure.UnionFind import *` みたいな記法で import を行っている

現状，`from src.data_structure.UnionFind import aaa, bbb` のようにしても`from src.data_structure.UnionFind import *` にしても元のファイルを全て展開するようになっています（個別の import に対応するのが面倒だったので...）

```
python3 expansion.py A.py exp.py
```
みたいにすると，`A.py` 内の import が全て置き換わった状態で `exp.py` に展開されます

