def test(blocked, source, target):
    possible = set()
    stack = [tuple(source), ]
    possible.add(tuple(source))
    limit = len(blocked) * (len(blocked) + 1) // 2 - len(blocked)
    blocked = [tuple(x) for x in blocked]
    count = 1
    while stack:
        cur = stack.pop()
        enum = ((0, -1), (0, 1), (1, 0), (-1, 0))
        for e in enum:
            c = tuple((cur[0] + e[0], cur[1] + e[1]))
            if c == target:
                return 2
            if 0 <= c[0] < 10 ** 6 and 0 <= c[1] < 10 ** 6 and c not in blocked:
                if not c in possible:
                    possible.add(c)
                    stack.append(c)
                    count += 1
                    if count > limit:
                        return 1
    return 0


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        source = tuple(source)
        target = tuple(target)
        r1 = test(blocked, source, target)
        if r1 == 0:
            return False
        if r1 == 2:
            return True
        r2 = test(blocked, target, source)
        if r2 == 0:
            return False
        return True

s = Solution()
# print(s.isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))
# print(s.isEscapePossible(blocked = [], source = [0,0], target = [999999,999999]))
print(s.isEscapePossible(blocked = [[0,3],[1,0],[1,1],[1,2],[1,3]], source = [0,0], target = [0, 2]))
