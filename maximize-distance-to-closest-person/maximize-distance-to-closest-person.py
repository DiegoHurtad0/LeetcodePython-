class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        m, tmp, first = 0, 0, None
        
        for s in seats:
            if s == 1:
                if first == None:
                    first = tmp
                m, tmp = max(m,tmp), 0
            tmp += 1
		
        Output = max(first, m//2, tmp-1)
        return Output