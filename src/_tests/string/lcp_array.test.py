# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_substrings
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.string.suffix_array import suffix_array, lcp_array


S = input()
sa = suffix_array(S)
lcp = lcp_array(S, sa)
n = len(S)
print(n * (n + 1) // 2 - sum(lcp))
