class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        from collections import defaultdict
        res = defaultdict(int)
        s = []
        recursive = 0
        for l in logs:
            i, t, time = l.split(":")
            if t == "start":
                s.append([int(i),int(time),int(time)])
            else:
                _, origin_start, start = s.pop()
                delta = int(time) - start + 1
                res[int(i)] += delta
                if s:
                    s[-1][-1] += (int(time) - origin_start + 1)
                if not s:
                    recursive = 0
        return [res[k] for k in sorted(res.keys())]

s = Solution()
print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
print(s.exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
print(s.exclusiveTime(1, ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]))
