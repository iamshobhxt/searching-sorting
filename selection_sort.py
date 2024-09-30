def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
            arr[i],arr[min]=arr[min],arr[i]

data = [23,43,2,4,54,34,3]
print("unsorted array :",data)
selection_sort(data)
print("sorted array :",data)                
