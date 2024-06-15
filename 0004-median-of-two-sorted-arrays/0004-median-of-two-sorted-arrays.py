class Solution:
    def findMedianUtil(self, nums1, nums2):
        total = len(nums1) + len(nums2)
        start, end = 0, len(nums1) 

        while start <= end:
            mid1 = (start + end) // 2
            print(mid1)
            mid2 = (total+1)//2 - mid1
            print(mid2)

            l1, l2, r1, r2 = -10**7, -10**7, 10**7, 10**7
            if mid1 > 0:
                l1 = nums1[mid1-1]
            if mid2 > 0:
                l2 = nums2[mid2-1]
            if mid1 < len(nums1):
                r1 = nums1[mid1]
            if mid2 < len(nums2):
                r2 = nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1,l2)+min(r1,r2)) / 2.0
                else:
                    return max(l1,l2)
            
            if l1 > r2:
                end = mid1 - 1

            if l2 > r1:
                start = mid1 + 1

        return 0


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m <= n:
            return self.findMedianUtil(nums1, nums2)
        else:
            return self.findMedianUtil(nums2, nums1)
        

        