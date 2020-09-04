class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k > len(bloomDay):
            return -1

        from heapq import *
        heap = [(bloomDay[i], i) for i in range(len(bloomDay))]
        heapify(heap)

        cur = 0
        blooms_left = dict()
        blooms_right = dict()
        while True:
            day, pos = heappop(heap)
            if pos-1 in blooms_left and pos+1 in blooms_right:
                left = blooms_left[pos-1]
                right = blooms_right[pos+1]
                cur -= (right - pos) // k
                cur -= (pos - left) // k
                cur += (right - left + 1) // k
                blooms_left[right] = left
                blooms_right[left] = right
            elif pos-1 in blooms_left:
                left = blooms_left[pos-1]
                blooms_right[left] = pos
                blooms_left[pos] = left
                if (pos - left + 1) % k == 0:
                    cur += 1
            elif pos+1 in blooms_right:
                right = blooms_right[pos+1]
                blooms_left[right] = pos
                blooms_right[pos] = right
                if (right - pos + 1) % k == 0:
                    cur += 1
            else:
                blooms_left[pos] = pos
                blooms_right[pos] = pos
                if k == 1:
                    cur += 1
            if cur == m:
                return day
