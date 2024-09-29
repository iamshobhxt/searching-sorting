def bubble_sort(arr, size):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                 arr[j],arr[j+1]=arr[j+1],arr[j]

data = [23,34,2,4,5,32,6]
n= len(data)
bubble_sort(data,n)
print(data)