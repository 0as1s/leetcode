class Solution(object):
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        from collections import defaultdict
        occu_dic = defaultdict(int)
        sum_dic = defaultdict(int)
        r = 0
        for i in A:
            r += sum_dic[A-i]
            for o in occu_dic:
                sum_dic[o+i] += occu_dic[o]
            occu_dic[i] += 1
        return r % (10**9+7)
