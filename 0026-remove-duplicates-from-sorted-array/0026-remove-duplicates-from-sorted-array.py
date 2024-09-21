class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if len(nums) == 0:
            return count

        curr_ptr, prev_ptr, curr_num = 1, 1, nums[0]
        while curr_ptr < len(nums):
            if nums[curr_ptr] != curr_num:
                count += 1
                nums[prev_ptr] = nums[curr_ptr]
                prev_ptr += 1

                curr_num = nums[curr_ptr]
            curr_ptr += 1

        return count + 1

        