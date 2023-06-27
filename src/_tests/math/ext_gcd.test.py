# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E&lang=ja
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))


def ext_gcd(a, b):
    """
    return (x, y, gcd(a, b)) s.t. ax + by = gcd(a, b)
    """
    if b == 0:
        return 1, 0, a
    else:
        y, x, g = ext_gcd(b, a % b)
        return x, y - (a // b) * x, g
