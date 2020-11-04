class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        nums = [0]
        down = 0
        up = 0
        for s in S:
            if s == "I":
                up += 1
                nums.append(up)
            if s == "D":
                down -= 1
                nums.append(down)
        m = min(nums)
        return [x - m for x in nums]