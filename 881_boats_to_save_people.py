class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        left = 0
        right = len(people) - 1
        boats = 0
        while left < right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            boats += 1
        if left == right:
            boats += 1
        return boats


s = Solution()
print(s.numRescueBoats([3,5,3,4], 5))

