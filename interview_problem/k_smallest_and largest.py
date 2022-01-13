#k largest element min heap
from heapq import heappop, heappush, heapify
a="I  to ammmmmmmmmm good Programmmer"
lst=a.split(" ")
#making pair
ans=[]
#min heap 
#for max heap multplie -1
heapp=heapify(ans)
for i in lst:
    heappush(ans,(len(i),i))
    if len(ans)>3:
        heappop(ans)
        print(ans)
print(ans[0])
#k  smallest element max  heap 
#time complexity nlogk