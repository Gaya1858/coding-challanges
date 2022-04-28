# Given an array of integers, return a new array where each elements in the new array is the number of smaller
# elements to the right of that element in the original input array.
# there are 2 ways to solve the problem
# 1. naive approach which is the brute force algo and its TC is O(N^2)
# 2. is using bisect model from python and its TC is O(NlogN)

import bisect
# 1
def smallerEleRight(nums):
    l = 0
    newlst = []
    while l < len(nums):
        value = nums[l]
        count = 0

        for i in range(l+1,len(nums)):
            if nums[i] < value:
                count += 1
        newlst.append(count)
        l += 1
    return newlst

def smaller_bisect(nums):
    result = []
    seen = []
    for i in reversed(nums):
        n = bisect.bisect_left(seen, i)
        result.append(n)
        bisect.insort(seen, i)
    return list(reversed(seen))

nums = [3,4,9,6,1]
print("Naive approach",smallerEleRight(nums))
print("Bisect model used",smaller_bisect(nums))