class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l =  len(nums)
        if l < 2:
            return False
        
        nums.sort()
        set_n =  set(nums)
        if len(nums) == len(set_n):
            return False
        return True