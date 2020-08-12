class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1
        if len(cost) == 1:
            return 0
        start = 0
        end = 1
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        cur = delta[start]
        while start != end:
            if cur < 0:
                start -= 1
                if start == -1:
                    start = len(cost) - 1
                cur += delta[start]
            else:
                cur += delta[end]
                end += 1 
                if end == len(cost):
                    end = 0
        return start

