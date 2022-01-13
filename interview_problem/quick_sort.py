def partition(arr,si,ei):
    pivot=arr[si]
    #count no of element which less than pivot
    c=0
    for i in range(si,ei+1):
        if arr[i]<pivot:
            c+=1
    arr[c+si],arr[si]=arr[si],arr[c+si]
    pivot_index=si+c
    i=si
    j=ei
    while i<j:
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
    return pivot_index

def quick_sort(arr,si,ei):
    #base case 
    if si>=ei:
        return
    pivot_index=partition(arr,si,ei)
    quick_sort(arr,si,pivot_index-1)
    quick_sort(arr,pivot_index+1,ei)

arr=list(map(int,input().split()))
quick_sort(arr,0,len(arr)-1)
print(arr)