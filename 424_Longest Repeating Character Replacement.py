class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m = 0
        from queue import deque
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cur_m = 0
            left = k
            q = deque()
            for ll in s:
                if ll == l:
                    q.append(ll)
                    cur_m = max(cur_m, len(q))
                else:
                    if left > 0:
                        left -= 1
                        q.append(ll)
                        cur_m = max(cur_m, len(q))
                    else:
                        poped = q.popleft()
                        while poped == l:
                            poped = q.popleft()
                        left += 1
                        q.append(ll)
            m = max(cur_m, m)
        return m
