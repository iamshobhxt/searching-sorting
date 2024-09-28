def qucik_sort(arr, left, right):
    if(left < right):
        q = partition(arr, left, right)
        qucik_sort(arr, left, q-1)
        qucik_sort(arr, q+1, right)

def partition(arr, left, right):
    p = arr[right]
    i = left - 1
    for j in range(left, right):
        if(arr[j] <= p):
          i +=1
          arr[i],arr[j] = arr[j],arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i+1]      
    return i+1


data = [2, 34, 20, 29, 5, 23, 85]
size = len(data)
print("Unsorted Data :", data)
qucik_sort(data, 0, size-1)
print("Sorted Data :", data)