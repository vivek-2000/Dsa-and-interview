def merge(a1,a2,arr):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            arr[k]=a1[i]
            k+=1
            i+=1
        else:
            arr[k]=a2[j]
            k+=1
            j+=1
    while i<len(a1):
        arr[k]=a1[i]
        k+=1
        i+=1
    while j<len(a2):
        arr[k]=a2[j]
        j+=1
        k+=1
def mergesort(arr,si,ei):
    if len(arr)==0 or len(arr)==1:
        return
    mid=len(arr)//2
    a1=arr[:mid]
    a2=arr[mid:]
    mergesort(a1,si,mid)
    mergesort(a2,mid,ei)
    merge(a1,a2,arr)
    return arr
    
print(mergesort([1,4,3,2,9],0,5))
