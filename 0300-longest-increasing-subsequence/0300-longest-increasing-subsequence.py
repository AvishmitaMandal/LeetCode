class Solution:
    def binary_search(self, seq, target):
        ans = len(seq)
        low, high = 0, len(seq)-1

        while low <= high:
            mid = (low+high)//2

            if seq[mid] >= target:
                ans = min(ans,mid)
                high = mid-1
            else:
                low = mid + 1

        seq[ans] = target
        return seq
         

    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        n = len(nums)
        for x in range(n):
            if len(seq) == 0:
                seq.append(nums[x])
                continue
            if nums[x] > seq[len(seq)-1]:
                seq.append(nums[x])
            else:
                for y in range(len(seq)):
                    if seq[y] >= nums[x]:
                        seq[y] = nums[x]
                        break 
                seq = self.binary_search(seq, nums[x])

        return len(seq)
            
        