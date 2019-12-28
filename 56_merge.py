class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        r = []
        if not intervals:
            return []
        intervals = sorted(intervals)
        left = intervals[0][0]
        right = intervals[0][1]
        for i in intervals[1:]:
            if i[0] > right:
                r.append([left, right])
                left = i[0]
                right = i[1]
            else:
                right = max(right, i[1])
        r.append([left, right])
        return r

s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
print(s.merge([[1,4],[0,4]]))
print(s.merge([[1,4],]))
