class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        for i in candies:
            if i + extraCandies >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        return ans

        
