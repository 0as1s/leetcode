def s(left, result, used):
    if not left:
        result.append(list(used))
    for i in range(len(left)):
        temp = left[i]
        used.append(temp)
        left.remove(temp)
        # used = list(used)
        s(left, result, used)
        left.insert(i, temp)
        used.remove(left[i])


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        used = []
        result = []
        s(nums, result, used)
        return result


s_([1,2,3])

# function backtrack(list, tempList, nums) {
#     if (tempList.length === nums.length) return list.push([...tempList]);
#     for(let i = 0; i < nums.length; i++) {
#         if (tempList.includes(nums[i])) continue;
#         tempList.push(nums[i]);
#         backtrack(list, tempList, nums);
#         tempList.pop();
#     }
# }
