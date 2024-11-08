from itertools import groupby

def compressedString(word):
    g = groupby(word)
    
    ans = []
    for c, v in g:
        k = len(list(v))
        print(k)
        while k:
            x = min(9, k)
            ans.append(str(x) + c)
            k -= x
    return "".join(ans)

word = "aaabbaaea"
print(compressedString(word))