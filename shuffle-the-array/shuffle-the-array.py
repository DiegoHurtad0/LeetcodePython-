class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        Output=[]
        for i in range(n):
            Output+=[nums[i],nums[i+n]]
        return Output