class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        from_l = []
        most_l = -float("Inf")
        for i, d in enumerate(dominoes):
            if d == "R":
                most_l = i
            if d == "L":
                most_l = -float("Inf")
            from_l.append(i - most_l)
        from_r = [float("Inf")] * len(dominoes)
        most_r = float("Inf")
        for i in range(len(dominoes)-1, -1, -1):
            d = dominoes[i]
            if d == "L":
                most_r = i
            if d == "L":
                most_r = float("Inf")
            from_r[i] = most_r-i
        r = []
        for x, y in zip(from_l, from_r):
            if x == y:
                r.append(".")
            if x > y:
                r.append("L")
            if y > x:
                r.append("R")
        return "".join(r)
