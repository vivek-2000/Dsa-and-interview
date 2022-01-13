"""
  1
 121
12321

"""
#n-1
n=int(input())
k=n-1
for i in range(1,n+1):
    print(" "*k,end=" ")
    k-=1
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")

    print()
    

