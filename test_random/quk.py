def partition(arr,si,ei):
    pivot=arr[si]
    c=0
    for i in range(si,ei+1):
        if arr[i]<pivot:
            c+=1
    arr[si+c],arr[si]=arr[si],arr[si+c]
    i=si
    j=ei
    while i<j:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
    return (c+si)
def quicksort(arr,si,ei):
    if si>=ei:
        return
    part=partition(arr,si,ei)
    quicksort(arr,si,part-1)
    quicksort(arr,part+1,ei)
arr=[5,7,8,9,1,3,6,2,0]
quicksort(arr,0,len(arr)-1)
print(arr)