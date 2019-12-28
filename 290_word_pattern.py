class Solution(object):

    def wordPattern(self, pattern, str):
        d = dict()
        temp = str.split(' ')
        if not len(temp) == len(pattern):
            return False
        for a, b in zip(pattern, temp):
            if a in d.keys():
                if b != d[a]:
                    return False
            else:
                if b in d.values():
                    return False
                d[a] = b
        return True
