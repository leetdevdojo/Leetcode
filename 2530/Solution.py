import math
import heapq
def maxKelements(nums, k):
    h = [-v for v in nums]
    heapq.heapify(h)
    ans = 0
    for _ in range(k):
        v = -heapq.heappop(h)
        ans += v
        heapq.heappush(h, -(math.ceil(v / 3)))
    return ans

print(maxKelements([1,10,3,3,3], 4))
