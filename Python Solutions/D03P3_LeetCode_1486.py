# Python3 code coming soon
class Solution(object):
    def xorOperation(self, n, start):
        res = t = start
        for i in range(1, n):
            t = t+2  
            res = res ^ t
        return res
