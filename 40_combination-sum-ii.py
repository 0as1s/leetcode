def s_(nums, target, result, used):
    if target < 0:
        return
    if target == 0:
        result.add(tuple(sorted(used)))

    pre = -1
    for n in nums:
        if pre == n:
            continue
        if n > target:
            return
        temp1 = list(nums)
        temp2 = list(used)
        temp1.remove(n)
        temp2.append(n)
        s_(temp1, target-n, result, temp2)
        pre = n


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = set()
        used = []
        s_(candidates, target, result, used)

        return result


s([10,1,2,7,6,1,5], 8)


# function backtrack(list, tempList, nums, remain, start) {
#     if (remain < 0) return;
#     else if (remain === 0) return list.push([...tempList]);
#     for (let i = start; i < nums.length; i++) {
#       // 和39.combination-sum 的其中一个区别就是这道题candidates可能有重复
#       // 代码表示就是下面这一行
#       if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
#       tempList.push(nums[i]);
#       backtrack(list, tempList, nums, remain - nums[i], i + 1); // i + 1代表不可以重复利用， i 代表数字可以重复使用
#       tempList.pop();
#     }
#   }

# 用start来实现代码中的remove，可以极大减少内存和时间的用量