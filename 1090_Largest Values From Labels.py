class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        if not values:
            return 0
        pair = list(zip(values, labels))
        pair = sorted(pair, key=lambda x: -x[0])
        from collections import defaultdict
        count = defaultdict(int)
        sum = 0
        for p in pair:
            if num_wanted == 0:
                return sum
            if count[p[1]] < use_limit:
                sum += p[0]
                num_wanted -= 1
                count[p[1]] += 1
        return sum