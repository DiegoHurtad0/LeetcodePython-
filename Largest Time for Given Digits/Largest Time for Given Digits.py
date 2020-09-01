class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        "23:41"
        """
        lista = list(permutations(sorted(A,reverse=True)))
        
        for h1, h2, m1, m2 in lista:
            if h1 * 10 + h2 < 24 and m1 * 10 + m2 < 60:
                Output = str(h1) + str(h2) + ':' + str(m1) + str(m2)
                return Output
        
        return ''