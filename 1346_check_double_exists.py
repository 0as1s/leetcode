class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        wanted = set()
        for i in arr:
            if i in wanted:
                return True
            wanted.add(i*2)
            if i % 2 == 1:
                continue
            wanted.add(i//2)
