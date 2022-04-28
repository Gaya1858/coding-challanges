# Given an array of integers, return a new array such that each element in index i of the new array is the productr of
# all the numbers in the original array except the one at i
# there are two ways to solve the problem
# 1. using product of all elements in the array
# 2. two way algorithm

# 1
from typing import List


def getProductDivision(nums: List[int]) -> List[int]:
    product = 1
    for i in nums:
        product *= i
    return [product//x for x in nums]

def getProductTwoWay(nums: List[int]) -> List[int]:

    result = []
    pre = []
    for i in nums:
        if pre:
            pre.append(pre[-1]*i)
        else:
            pre.append(i)
    suf = []
    for j in reversed(nums):
        if suf:
            suf.append(suf[-1]*j)
        else:
            suf.append(j)
    suf =list(reversed(suf))
    for i in range(len(nums)):
        if i == 0:
            result.append(suf[i+1])
        elif i == len(nums)-1:
            result.append(pre[i-1])
        else:
            result.append(pre[i-1] * suf[i+1])
    return result

nums = [1,2,3,4,5]
print("two way algorithm",getProductTwoWay(nums))
print("using division   ",getProductDivision(nums))