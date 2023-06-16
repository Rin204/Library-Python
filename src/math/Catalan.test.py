# verification-helper: PROBLEM https://yukicoder.me/problems/no/790
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))
from src.math.Combination import Combination


n = int(input())
C = Combination(n)
print(C.Catalan(n))
