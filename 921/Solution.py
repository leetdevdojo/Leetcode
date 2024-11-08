def minAddToMakeValid(s):
    stk = []
    for c in s:
        if c == ')' and stk and stk[-1] == '(':
            stk.pop()
        else:
            stk.append(c)
    return len(stk)  

print(minAddToMakeValid("()))(("))