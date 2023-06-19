#Moore's Voting Algorithm is an efficient algorithm used 
#to find the majority element in an array.
#The majority element is defined as the element that appears more than ⌊n/2⌋ times, 
#where n is the length of the array. 
#The algorithm guarantees to find the majority element if it exists.
def majority_element(nums):
    # Step 1: Find the potential majority element
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify if the potential majority element is the majority
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    if count > len(nums) // 2:
        return candidate
    else:
        return None
