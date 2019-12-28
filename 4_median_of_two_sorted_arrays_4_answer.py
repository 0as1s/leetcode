class Solution:
    # @return a float

    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B, l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        print A, B, k
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's
            # not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


nums1 = range(10)
nums2 = range(20)
s = Solution()
s.findMedianSortedArrays(nums1, nums2)
