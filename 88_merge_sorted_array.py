class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0, m):
            nums1[m + n - i - 1] = nums1[m - 1 - i]
        i = 0
        j = 0
        while True:
            if j == n:
                return
            if i == m:
                for k in range(i + j, m + n):
                    nums1[k] = nums2[j]
                    j += 1
                # nums1[i + j, m + n] = nums2[j, n]
                return
            if nums1[i + n] < nums2[j]:
                nums1[i + j] = nums1[i + n]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
nums1 = [3, 4, 0, 0, 0, 0, 0, 0]
nums2 = [1, 2, 6, 7, 8, 0, 0, 0, 0]
m = 2
n = 5

s = Solution()
# s.merge(nums1, m, nums2, 5)
s.merge(nums2, n, nums1, m)
print nums2
