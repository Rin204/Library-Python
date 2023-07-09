# verification-helper: PROBLEM https://yukicoder.me/problems/1013
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.string.AhoCorasick import AhoCorasick


S = input()
n = int(input())
ac = AhoCorasick()
for i in range(n):
    T = input()
    ac.register(T)

ac.build()
match = ac.search(S)
ls = len(S)
ans = 0
for row in match:
    ans += len(row)

print(ans)
