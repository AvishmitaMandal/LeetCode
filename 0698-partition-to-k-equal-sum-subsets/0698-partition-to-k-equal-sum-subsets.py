class Solution:
    def isKPartitionPossibleUtil(self, nums: List, visited: List, target: int, k: int, total: int, ptr: int) -> bool:
        if k == 1:
            return True

        if total == target:
            return self.isKPartitionPossibleUtil(nums, visited, target, k-1, 0, 0)

        for x in range(ptr, len(nums)):
            if visited[x] == 0 and total + nums[x] <= target:
                visited[x] = 1
                if self.isKPartitionPossibleUtil(nums, visited, target, k, total + nums[x], x+1):
                    return True
                visited[x] = 0

        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse = True)
        
        n = len(nums)
        visited = [0 for _ in range(n)]

        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target = total_sum // k
        if nums[0] > target:
            return False
        
        if k == 1:
            return True

        if self.isKPartitionPossibleUtil(nums, visited, target, k, 0, 0):
            return True
        
        return False
        