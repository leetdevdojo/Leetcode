def minChanges(s):
        return sum(a != b for a, b in zip(s[::2], s[1::2]))

s = "000"
print(minChanges(s))