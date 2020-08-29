class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        Output=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                Output.append(True)
            else:
                Output.append(False)
        return Output