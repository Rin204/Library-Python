def make_popcount(n):
    print("def popcount(x):")
    le = 1
    while le < n:
        le *= 2
    five = "5" * n
    print(f"    x = (x & 0x{five}) + ((x >> 1) & 0x{five})")
    three = "3" * n
    print(f"    x = (x & 0x{three}) + ((x >> 2) & 0x{three})")
    d = 1
    shift = 4
    while shift < le:
        S = []
        for _ in range((le + 2 * d - 1) // (2 * d)):
            S += ["0"] * d
            S += ["f"] * d
        S = "".join(S[-n:])
        print(f"    x = (x & 0x{S}) + ((x >> {shift}) & 0x{S})")
        shift <<= 1
        d <<= 1
    print("    return x")
