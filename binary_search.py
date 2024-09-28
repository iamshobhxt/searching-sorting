def binary_search(arr, left, right, val):
    while(left <= right):
        mid = (left + right)//2
        if(arr[mid] == val):
           return mid
        elif(arr[mid] > val ):
           right = mid - 1
        else:
           left = mid + 1
    return -1   

data = [1,2,3,4,5,6]
size = len(data)
n = 1
ans = binary_search(data, 0, size-1, n)
if(ans == -1):
    print(" index not found")
else:
    print(" index found ",ans)    
