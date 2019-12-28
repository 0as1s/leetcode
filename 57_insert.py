class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval, ]
        if newInterval[1] < intervals[0][0]:
            temp = [newInterval, ]
            temp.extend(intervals)
            return temp
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        if newInterval[0] < intervals[0][0] and newInterval[1] > intervals[-1][1]:
            return [newInterval, ]
        if len(intervals) == 1:
            return [[min(intervals[0][0], newInterval[0]), max(intervals[0][1], newInterval[1])],]
        left = 0
        right = len(intervals)
        L = newInterval[0]
        L_index = 0
        while True:
            mid = (left + right) // 2
            if intervals[mid][0] <= newInterval[0] <= intervals[mid][1]:
                L = intervals[mid][0]
                L_index = mid
                break
            if right - left == 1:
                L_index = right
                L = newInterval[0]
                break
            if newInterval[0] < intervals[mid][0]:
                right = mid
            else:
                left = mid
        # print(L)
        R = newInterval[1]
        left = 0
        right = len(intervals)
        while True:
            mid = (left + right) // 2
            if intervals[mid][0] <= newInterval[1] <= intervals[mid][1]:
                R = intervals[mid][1]
                R_index = mid
                break
            if right - left == 1:
                R = newInterval[1]
                R_index = left
                break
            if newInterval[1] < intervals[mid][0]:
                right = mid
            else:
                left = mid
        if L <= intervals[0][0] and R >= intervals[-1][1]:
            return [[L, R], ]
        temp = []
        # temp.extend(intervals[:L_index])
        # temp.append([L, R])
        # temp.extend(intervals[R_index:])
        # return temp

        for i in range(len(intervals)):
            if intervals[i][1] < L:
                temp.append(intervals[i])
            if intervals[i][0] > R:
                temp.append(intervals[i])
        for i in range(len(temp)):
            if temp[i][1] > L:
                temp.insert(i, [L, R])
                return temp

s = Solution()
print(s.insert([[1,5],], [2,7]))
print(s.insert([[1,5],[6,8]], [3,9]))
print(s.insert(intervals = [[1,5],], newInterval = [0,0]))
print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))