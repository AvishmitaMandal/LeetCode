class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1 = [1,2,3,0,0,0], nums2 = [2,5,6]
        """

        temp = []
        x, y = 0, 0
        while x < m and y < len(nums2):
            if nums1[x] <= nums2[y] :
                temp.append(nums1[x])
                x += 1
            else:
                temp.append(nums2[y])
                y += 1

        while x < m:
            temp.append(nums1[x])
            x += 1

        while y < len(nums2):
            temp.append(nums2[y])
            y += 1

        print(temp)

        for x in range(len(temp)):
            nums1[x] = temp[x]
        