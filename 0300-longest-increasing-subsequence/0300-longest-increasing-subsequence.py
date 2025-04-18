class Solution:
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

        return len(seq)
            
        