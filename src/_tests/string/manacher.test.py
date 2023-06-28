# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.string.manacher import manacher


S = input()
res = manacher(S)
print(*res)
