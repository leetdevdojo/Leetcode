def minSwaps(s):
    x = 0
    for c in s:
        if c == "[":
            x += 1
        elif x:
            x -= 1
        print(x)
    return (x + 1) >> 1


print(minSwaps("]]][[["))