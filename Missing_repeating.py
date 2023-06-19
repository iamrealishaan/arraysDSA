def missing_repeating_number(nums):
    n = len(nums)
    repeating_num = 0
    missing_num = 0
    # finding the repeating number
    for i in range(n):
        if nums[abs(nums[i])-1] > 0:
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i])-1]
        else:
            repeating_num = abs(nums[i])
    #finding the missing nmumber
    for i in range(n):
        if nums[i]>0:
            missing_num = i+1
            break
    return missing_num, repeating_num

nums = [1,2,2,2,4,3,6]
missing,repeating = missing_repeating_number(nums)
print("Missing Number is:", missing)
print("Repeating Number is:", repeating)



