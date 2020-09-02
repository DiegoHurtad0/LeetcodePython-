class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)<0:
            return max(nums)
        
        suma, Output = 0, 0
        
        for num in nums:
            suma = max(0, suma + num)
            Output = max(suma, Output)
        return Output