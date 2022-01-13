#reverse array
a=[1,2,3,4]
start=0
end=len(a)-1
while start<=end:
    a[start],a[end]=a[end],a[start]
    start+=1
    end-=1
print(a)

#reverse string
astr="vivek patel"
revstring=""
for i in astr:
    revstring=i+revstring #important 
print(revstring)
print(astr[::-1])