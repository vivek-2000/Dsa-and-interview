def countDuplicate(numbers):
    ans=[]
    count=0
    for i in numbers:
        if i in ans:
            count+=1
        else:
            ans.append(i)
    return count
print(countDuplicate([1,3,1,4,5,6,3,2]))