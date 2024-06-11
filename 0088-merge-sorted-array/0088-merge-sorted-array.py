class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums = []
        for x in range(m):
            nums.append(nums1[x])

        it1, it2, x = 0, 0, 0
        while it1 < m and it2 < n:
            if it1 == m or it2 == n:
                break

            if nums[it1] <= nums2[it2]:
                nums1[x] = nums[it1]
                it1 += 1

            else:
                nums1[x] = nums2[it2]
                it2 += 1

            x += 1

        i, j = it1, it2

        if it1 == m:
            while j < n and x < m+n:
                nums1[x] = nums2[j]
                j += 1
                x += 1

        elif it2 == n:
            while i < m and x < m+n:
                nums1[x] = nums[i]
                i += 1
                x += 1

        return nums1
        