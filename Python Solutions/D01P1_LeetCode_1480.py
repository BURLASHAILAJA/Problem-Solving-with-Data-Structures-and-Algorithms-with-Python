class Solution(object):
    def runningSum(self, nums):
        new_list=[]
        s=0
        for i in nums:
            s=s+i 
            new_list.append(s) 
        return new_list
