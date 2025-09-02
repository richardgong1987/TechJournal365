

def isMatch(s: str, p: str) -> bool:
    i = j = 0  # i -> s, j -> p
    star = -1  # last '*' index in p
    match = 0  # s index matched by last '*'

    while i < len(s):
        if j < len(p) and (p[j] == s[i] or p[j] == '?'):
            # direct match or '?'
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            # record star and try '*' = empty
            star = j
            match = i
            j += 1
            print(fr"star: {star}, match: {match}, j: {j}, i: {i}")
        elif star != -1:
            # mismatch: expand previous '*'
            j = star + 1
            match += 1
            i = match
            print(fr"star: {star}, match: {match}, j: {j}, i: {i}")
        else:
            return False

    # s is finished; remaining p must be all '*'
    while j < len(p) and p[j] == '*':
        j += 1

    return j == len(p)


print(isMatch("abc", "*a"))