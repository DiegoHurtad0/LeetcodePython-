class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        
        for i in range(max(nums)+1):
            count[i] += count[i-1]
        return [count[i-1] for i in nums]