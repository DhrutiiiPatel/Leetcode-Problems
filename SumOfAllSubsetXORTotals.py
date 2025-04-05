class Solution:
    def subsetXORSum(self, nums):
        return reduce(or_, nums)<<(len(nums)-1)
