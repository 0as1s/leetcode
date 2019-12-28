class Solution(object):

    def isNumber(self, s):
        ss = s.strip()
        try:
            float(ss)
        except ValueError:
            return False
        return True
