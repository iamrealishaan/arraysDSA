def find_second_largest_element(arr):
    if len(arr)<2:
        return None
    sorted_arr = sorted(arr,reverse = True)
    return sorted_arr[1]
my_array = [3,5,1,45,2,21]
result = find_second_largest_element(my_array)
print(result)
