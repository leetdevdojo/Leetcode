import heapq
def minGroups(intervals):
    start = []
    end =[]
    for l,r in intervals:
        start.append(l)
        end.append(r)
    start.sort()
    end.sort()

    i = 0
    j = 0
    res = 0
    g = 0
    while i < len(intervals):
        if start[i] <= end[j]:
            g += 1
            i += 1
        else:
            g-=1
            j+=1
        res=max(res,g)
    return res


intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
print(minGroups(intervals))