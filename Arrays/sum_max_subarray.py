# given an array of integers, return maximum sum of
# return subarrays
# there 3 different approach to this proble . As usual the brute force first and then
# 1 brute force and it runs TC O(N^3)
# 2. Kanane's algo and TC is O(N)
# 3. wrap around the arrya to find the max subarray

#1
def max_subarray(nums):
    max_value = 0
    for i in range(len(nums)-1):
        for j in range(i, len(nums)+1):
            max_value = max(max_value, sum(nums[i:j]))
    return max_value

#2
def max_subarray_kadane(nums):
    max_one =  max_last = 0
    for x in nums:
        max_one = max(x, x+max_one)
        max_last = max(max_last, max_one)
    return max_last

#3

def max_subarray_circular(nums):

    max_subarray_wrap = sum(nums) - min_subarrauy_wrap(nums)

    return max(max_subarray_kadane(nums),max_subarray_wrap)

def min_subarrauy_wrap(nums):
    min_end_here = min_so_far = 0
    for x in nums:
        min_end_here = min(x, min_end_here + x)
        min_so_far = min(min_end_here, min_so_far)
    return min_so_far
nums =[8, -1, 3,4]
print("Brute force: ",max_subarray(nums))
print("Kadane's algo: ",max_subarray_kadane(nums))
print("wrap around max subarray: ", max_subarray_circular(nums))