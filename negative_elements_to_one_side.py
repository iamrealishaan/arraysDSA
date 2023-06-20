def push_negative_right_side(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

arr = [1, 2, -3, -14]
result = push_negative_right_side(arr)
print("New array is:", result)
