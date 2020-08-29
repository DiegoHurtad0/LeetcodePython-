class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp={}
        Output=0
        for n in nums:
            if not n in tmp:
                tmp[n]=0
            tmp[n]+=1
        
        for n in tmp:
            n=tmp[n]
            Output+=(n*(n-1)//2)
            
        return Output