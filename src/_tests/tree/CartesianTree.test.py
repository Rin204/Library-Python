# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cartesian_tree
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.tree.CartesianTree import CartesianTree


n = int(input())
A = list(map(int, input().split()))
print(*CartesianTree(A))
