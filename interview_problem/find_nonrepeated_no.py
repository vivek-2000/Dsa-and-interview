arr=[1,1,3,3,4,5,5,6,6]
x=arr[0]
for i in range(1,len(arr)):
    x=x^arr[i]
print(x)