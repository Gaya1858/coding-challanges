# given an array of integers that are out of order, determine the bounds of the smallesr window that must be sorted
# in order for the entire array to be sorted.
# example: [3,7,5,6,9] should return (1,3)

# sorted solution and it is O(NlogN)
def window(nums):
    left, right = None, None
    s =sorted(nums)

    for i in range(len(nums)):
        if nums[i] != s[i] and left is None:
            left = i
        elif nums[i] != s[i]:
            right = i
    return left, right

# loop through actual and reversed array to get O(N) time
def windowN(nums):

    left, right  = None, None
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(len(nums)):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            right = i
    for i in range(len(nums)-1, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            left = i
    return left, right

nums = [3,7,5,6,9]
print(window(nums))
print(windowN(nums))