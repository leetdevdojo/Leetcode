def resultsArray(nums, k):
        n = len(nums)
        f = [1] * n
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                f[i] = f[i - 1] + 1
        return [nums[i] if f[i] >= k else -1 for i in range(k - 1, n)]

nums = [1,2,3,4,3,2,5]
k = 3
print(resultsArray(nums, k))
