# verification-helper: PROBLEM https://yukicoder.me/problems/no/649

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from src.data_structure.BIT import BIT

Q, k = map(int, input().split())
Query = []
X = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        X.append(query[1])
        Query.append(query[1])
    else:
        Query.append(-1)

X = sorted(set(X))
dic = {x: i for i, x in enumerate(X)}

bit = BIT(len(dic))
for q in Query:
    if q == -1:
        p = bit.lower_bound(k) - 1
        if p == len(X):
            print(-1)
        else:
            print(X[p])
            bit.add(p, -1)
    else:
        bit.add(dic[q], 1)
