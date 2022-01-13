A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

def funct(arr):
    dct={}
    for i in arr:
        if i in dct:
            dct[i]+=1
        else:
            dct[i]=1
    ans=[]
    for key,value in dct.items():
        if value>1:
            ans.append(key)
    return ans

