class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        l, Output=len(nums),[]
        
        for i in range(l):
            Output.insert(index[i],nums[i])
        
        return Output
        