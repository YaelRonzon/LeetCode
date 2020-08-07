# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def two_sum(nums, target):
    for i, n in enumerate(nums):
        for j, m in enumerate(nums):
            if i != j:
                if n + m == target:
                    return [i, j]

# The following version is more efficient, since uses just one interation keeping the linear time.

def two_sum_v2(nums, target):
    for i, n in enumerate(nums):
        second = target - n
        if second in nums and nums.index(second) != i:
                return [i, nums.index(second)]
        

