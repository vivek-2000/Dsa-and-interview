def fib(n):
    if n==0 or n==1:
        return n
    f1=fib(n-1)
    f2=fib(n-2)
    return f1+f2
n=int(input())
print(fib(n))
for i in range(n):
    print(fib(i),end=" ")