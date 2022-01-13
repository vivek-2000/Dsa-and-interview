from heapq import heappop, heappush, heapify
a="I am good Programmmer"
lst=a.split(" ")
#making pair
ans=[]
for i in lst:
    ans.append((len(i),i))
    
heapp=heapify(ans)
for i in range(3):
    result=heappop(ans)
print(result[0]*-1,result[1])
