# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.string.KMP import kmp_search


T = input()
P = input()
ans = kmp_search(T, P)
if ans:
    print(*ans, sep="\n")
