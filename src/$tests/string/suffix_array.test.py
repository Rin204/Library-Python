# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.string.suffix_array import suffix_array


S = input()
sa = suffix_array(S)
print(*sa)
