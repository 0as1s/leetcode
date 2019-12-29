from random import random

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist = blacklist
        self.bs = set(blacklist)
        self.N = N

    def pick(self):
        """
        :rtype: int
        """
        r = int(random() * self.N)
        if r not in self.bs:
            return r
        for b in self.blacklist:
            r = r ^ b
            # if r not in self.bs:
            #     return r
        print(r)
        return r


s = Solution(10,[1,2,3,4,5,6])
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()
s.pick()

