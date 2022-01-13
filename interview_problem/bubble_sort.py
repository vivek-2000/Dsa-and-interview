#Reapetedly swap two adjacent elements if they are in wrong order
#n-1 times
# ith iteration n-1
# O(N^2)

arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)