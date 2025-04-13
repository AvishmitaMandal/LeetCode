from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [100,4,200,1,3,2]
        n = 6
        mp = {100, 4, 200, 1, 3, 2}
        visited = {100}

        res = 1
        x = 0, nums[x] = 100
        start = 100
        end = 100

        BC :

        '''

        mp = defaultdict(int)
        n = len(nums)
        if n == 0:
            return 0
            
        for num in nums:
            mp[num] += 1

        visited = set()
        res = 1

        for x in range(n):
            if nums[x] not in visited:
                start, end = nums[x], nums[x]
                visited.add(nums[x])

                while start-1 in mp and start-1 not in visited:
                    start = start - 1
                    visited.add(start)

                while end+1 in mp and end+1 not in visited:
                    end = end + 1
                    visited.add(end)

                res = max(res, end-start+1)
                print(nums[x], res)
                print(start, end)

        return res

            

