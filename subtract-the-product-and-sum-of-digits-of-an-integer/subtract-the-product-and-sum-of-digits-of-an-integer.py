class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1
        sum = 0
        for digit in str(n):
            product *= int(digit)
            sum += int(digit)
        return product - sum
        