class Solution(object):
    def maxProduct(self, nums):
        nums=sorted(nums)
        s=(nums[-1]-1)*(nums[-2]-1)
        return s
