class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        Output = []
        for i in address:
            if i == '.':
                Output.append("[.]")
            else:
                Output.append(i)
        return "".join(Output)
        