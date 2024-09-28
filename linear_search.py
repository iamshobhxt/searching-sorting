def linear_search(arr, size, val):
    for i in range(len(arr)):
        if(arr[i]==val):
           return i
    return -1

data = [2,34,32,2,5,30,40,21,24]
size=len(data)
n=35
ans=linear_search(data,size,n)
if(ans == -1): 
    print("index not found")
else:    
    print("index found",ans)    