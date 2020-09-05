class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = {v:k for k, v in enumerate(S)}
        def cmp(x, y):
            return dic[x] - dic[y]

        T = list(T)
        to_sort = [x for x in T if x in dic]
        left = [x for x in T if x not in dic]
        return "".join(sorted(to_sort,cmp=cmp)) + "".join(left)