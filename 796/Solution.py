def rotateString(s, goal):
    i = len(s)-1
    c = 0
    while(i>=c):
        res = s[c:] + s[: c]
        if res == goal:
            return True
        c+=1

    return False


s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))
