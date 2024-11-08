def minLength(s):
    stack = [""]
    for i in s:
        if (i=="B" and stack[-1] == "A") or (i=="D" and stack[-1]=="C"):
            stack.pop()
        else:
            stack.append(i)
    return len(stack)-1



print(minLength("ABFCACDB"))