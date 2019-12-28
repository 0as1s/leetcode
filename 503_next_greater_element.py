class Solution(object):

    def nextGreaterElements(self, nums):
        if not nums:
            return []
        l = len(nums)
        for i in range(l - 1):
            if nums[i] <= nums[i + 1]:
                break
        else:
            return [-1] + [nums[0]] * (l - 1)

        result = [None] * l
        m = max(nums)
        for i in range(l):
            if nums[i] == m:
                index = i - 1 if not i - 1 == -1 else l - 1
                result[i] = -1
                if not nums[index] == m:
                    result[index] = i
        for i in range(result.index(-1)):
            if result[i] is None:
                cur = i + 1 if not i + 1 == l else 0
                while(True):
                    if nums[cur] > nums[i]:
                        result[i] = cur
                        break
                    cur = result[cur] if result[cur] else cur + 1
                    cur = 0 if cur == l else cur
        for i in range(result.index(-1) + 1, l):
            if result[i] is None:
                cur = i + 1 if not i + 1 == l else 0
                while(True):
                    if nums[cur] > nums[i]:
                        result[i] = cur
                        break
                    cur = result[cur] if result[cur] else cur + 1
                    cur = 0 if cur == l else cur

        for i in range(len(result)):
            if not result[i] == -1:
                result[i] = nums[result[i]]
        return result


s = Solution()
print s.nextGreaterElements([1, 2, 1])
