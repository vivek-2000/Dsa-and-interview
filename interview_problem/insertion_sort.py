#Values from the unsorted part are picked and placed at the correct position in the sorted part.
#e.g sort playing card
arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    curr=arr[i]
    j=i-1
    while j>=0 and arr[j]>curr:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=curr
print(arr)


