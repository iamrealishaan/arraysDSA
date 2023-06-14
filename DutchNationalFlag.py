def sort_array(num):
    low = 0
    mid = 0
    high = len(num)- 1
    while mid <= high:
        if num[mid] == 0:
            num[mid], num[low] =  num[low], num[mid]
            mid+=1
            low+=1
        elif num[mid] ==1:
            mid+=1
        elif num[mid] ==2:
            num[mid], num[high] = num[high], num[mid]
            high-= 1
    return num
my_arr = [0,0,1,2,1,2,0,2]
result = sort_array(my_arr)
print(result)
