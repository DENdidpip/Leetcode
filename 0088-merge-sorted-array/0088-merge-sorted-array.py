class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k, j, res = 0, 0, []
        while k < m and j < n:
            if nums1[k] <= nums2[j]:
                res.append(nums1[k])
                k += 1
            else:
                res.append(nums2[j])
                j += 1
        while k < m:
            res.append(nums1[k])
            k += 1
        while j < n:
            res.append(nums2[j])
            j += 1
        for i in range(m + n):
            nums1[i] = res[i]

