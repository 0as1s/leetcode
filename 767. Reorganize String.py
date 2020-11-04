from heapq import *
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(S)
        c = [[-v, k] for k, v in c.items()]
        heapify(c)
        if -c[0][0] > ((len(S) + 1) // 2):
            return ""
        t1 = heappop(c)
        r = [t1[1]]
        t1[0] += 1
        if t1[0] != 0:
            heappush(c, t1)
        while c:
            #print(c)
            t1 = heappop(c)
            if t1[1] != r[-1]:
                t1[0] += 1
                r.append(t1[1])
                if t1[0] != 0:
                    heappush(c, t1)
            else:
                if not c:
                    return ""
                t2 = heappop(c)
                heappush(c, t1)
                t2[0] += 1
                r.append(t2[1])
                if t2[0] != 0:
                    heappush(c, t2)
        return "".join(r)
