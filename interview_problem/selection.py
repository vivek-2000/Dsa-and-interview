#sorts an array by repeatedly finding the minimum element (considering ascending order)
#  from unsorted part and putting it at the beginning
#o(n^2)
arr=list(map(int,input().split()))
for i in range(len(arr)):
    min_indx=i
    for j in range(i+1,len(arr)):
        if arr[min_indx]>arr[j]:
            min_indx=j
    arr[i],arr[min_indx]=arr[min_indx],arr[i]
print(arr)