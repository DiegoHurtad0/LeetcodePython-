class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Output = []
        tmp = 0
        for i in nums:
            tmp+=i
            Output.append(tmp)
        return Output