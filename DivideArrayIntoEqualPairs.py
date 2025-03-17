class Solution:
    def divideArray(self, nums):
        K=0
        for x in nums:
            K^=(1<<x) 
        return K==0
        
