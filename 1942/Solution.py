import heapq
def smallestChair(times, targetFriend):

    times=[(t[0],t[1],i) for i,t in enumerate(times)]
    times.sort()
    arr =[]
    ava = [i for i in range(len(times))]

    for a ,l, i in times:
        while arr and arr[0][0] <= a:
            leve,chair = heapq.heappop(arr)
            heapq.heappush(ava,chair)
        chair = heapq.heappop(ava)
        heapq.heappush(arr,(l,chair))

        if i == targetFriend:
            return chair



times = [[1,4],[2,3],[4,6]]
targetFriend = 1
print(smallestChair(times,targetFriend))

