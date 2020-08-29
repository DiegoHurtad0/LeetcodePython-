class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        Output = list(s)
        l = len(s)
        for i in range(l):
            Output[indices[i]] = s[i]
        return "".join(Output)
        