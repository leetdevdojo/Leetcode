def maxWidthRamp(nums):
    maxarr = [0] * len(nums)
    res = 0
    prevmax = 0
    i =len(nums)-1
    for n in reversed(nums):
        maxarr[i] = max(n,prevmax)
        prevmax = maxarr[i]
        i -=1

    l = 0
    for r in range(len(nums)):
        while nums[l]>maxarr[r]:
            l+=1
        res = max(res,r - l)
    return res 


nums = [6,0,8,2,1,5]
print(maxWidthRamp(nums))