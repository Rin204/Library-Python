def partial_match_table(word):
    n = len(word)
    table = [0] * (n + 1)
    table[0] = -1

    i = 0
    j = 1
    while j < n:
        matched = word[i] == word[j]
        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i

    return table


def kmp_search(text, word):
    table = partial_match_table(word)
    n = len(text)

    i = p = 0
    ret = []
    while i < n:
        if text[i] == word[p]:
            i += 1
            p += 1
            if p == len(word):
                ret.append(i - p)
                p = table[p]
        else:
            p = table[p]
            if p < 0:
                i += 1
                p += 1

    return ret
