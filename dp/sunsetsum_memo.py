#User function Template for python3

class Solution:
    def fun(N,arr,summ,tab):
        
        if summ==0:
            return True
        if N==0:
            return False
        if tab[N-1][summ]!=-1:
            return tab[N-1][summ]
        #if given ele is greater than summ
        if arr[N-1]>summ:
            tab[N-1][summ]=Solution.fun(N-1,arr,summ,tab)
            return tab[N-1][summ]
        
        #else, check if sum can be obtained by any of the following 
    	#(a) including the last element 
    	#(b) excluding the last element

        else:
            tab[N-1][summ]=Solution.fun(N-1,arr,summ,tab) or Solution.fun(N-1,arr,summ-arr[N-1],tab) 
            return tab[N-1][summ] 
        
    def isSubsetSum (self, N, arr, summ):
        # code here 
        tab = [[-1 for i in range(summ+1)] for j in range(N+1)]
        if Solution.fun(N,arr,summ,tab):
            return True
        else:
            return False
        
        