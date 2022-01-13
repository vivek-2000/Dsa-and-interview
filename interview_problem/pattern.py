"""
5
    * 
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""
n=int(input())
#for spaces
k=n-1
for i in range(n):
    print(" "*k,end="")
    k=k-1
    print("* "*(i+1))
k=1
for i in range(n-1,-1,-1):
    print("* "*(i+1))
    print(" "*k,end="")
    k=k+1

