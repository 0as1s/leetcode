def s_(nums, target, result, used):
    # print(used, nums)
    if target < 0:
        return
    if target == 0:
        result.add(tuple(sorted(used)))

    for i, n in enumerate(nums):
        if n > target:
            continue
        used.append(n)
        s_(nums[i+1:], target-n, result, used)
        del(used[-1])


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # candidates = sorted(candidates)
        result = set()
        used = []
        s_(candidates, target, result, used)
        return result

s = Solution()
print(s.combinationSum2([2, 5, 2, 1, 2], 5))