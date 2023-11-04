class Solution(object):
    def numTeams(self, rating):
        c=0
        for  i in range (len(rating)):
            for j in range(i+1,len(rating)):
                for k in range(j+1,len(rating)):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        c+=1
        return c
                    
                    
