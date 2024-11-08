def minimumSteps(s):
    ln = 0 
    res = 0 
    
    for i in range(len(s)-1, -1, -1):
        p = s[i]
        if s[i] == "0":
            ln = max(ln, i + 1) 
        else:
            r = ln - (i + 1) 
            r = max(0, r) 
            res += r 
            ln -=1
    
    return res

print(minimumSteps("100010"))
