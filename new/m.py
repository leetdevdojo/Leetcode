def min_positive_sum_subarray(nums, l, r):
    n = len(nums)
    min_sum = float('inf')
    
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    for length in range(l, r + 1):
        for start in range(n - length + 1):
            subarray_sum = prefix_sum[start + length] - prefix_sum[start]
            if subarray_sum > 0:
                min_sum = min(min_sum, subarray_sum)
    
    return min_sum if min_sum != float('inf') else -1


nums = [17,13]
l = 1
r = 2
print(min_positive_sum_subarray(nums, l, r))  # Output: -1
