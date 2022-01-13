
class Solution:
    def fun(N,arr,summ):
        if summ==0:
            return True
        if N==0 and sum!=0:
            return False
        #if given ele is greater than summ
        if arr[N-1]>summ:
                return Solution.fun(N-1,arr,summ)
        
        #else, check if sum can be obtained by any of the following 
    	#(a) including the last element 
    	#(b) excluding the last element

        else:
            return Solution.fun(N-1,arr,summ-arr[N-1]) or Solution.fun(N-1,arr,summ)
        
    def isSubsetSum (self, N, arr, summ):
        # code here 
        if Solution.fun(N,arr,summ):
            return True
        else:
            return False
        