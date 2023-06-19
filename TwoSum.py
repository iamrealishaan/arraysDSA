#Given an array of integers nums and an integer target, 
#return indices of the two numbers such that they add up to target.
def TwoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return None

nums = [2, 7, 11, 15]
target = 9
result = TwoSum(nums, target)
print(result)
