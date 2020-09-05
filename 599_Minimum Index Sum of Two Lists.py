class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1 = sorted([(list1[i], i) for i in range(len(list1))])
        list2 = sorted([(list2[i], i) for i in range(len(list2))])

        m = float("Inf")
        l = 0
        r = 0
        result = []
        while True:
            sl = list1[l][0]
            sr = list2[r][0]
            if sl > sr:
                r += 1
                if r == len(list2):
                    break
            elif sr > sl:
                l += 1
                if l == len(list1):
                    break
            else:
                i1 = list1[l][1]
                i2 = list2[r][1]
                if i1 + i2 < m:
                    m = i1 + i2 
                    result = []
                    result.append(sl)
                if i1 + i2 == m:
                    result.append(sl)
                l += 1
                r += 1
                if r == len(list2) or l == len(list1):
                    break
        return set(result)