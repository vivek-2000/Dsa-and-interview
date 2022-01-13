def funct(mat,k):
    count=0
    if mat[0][0]<k:
        count+=1
        for i in range(1,k):
            if mat[0][0]*i<k:
                count+=1
    return count


mat=[[1,2,3],[1,2,3]]
k=3
print(funct(mat,k))