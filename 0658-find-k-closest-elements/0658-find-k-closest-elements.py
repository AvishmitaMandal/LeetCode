class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, 0
        curr_diff = 0

        res_start, res_end = 0,0
        min_diff = 10**9

        while end < len(arr):
            curr_diff += abs(arr[end]-x)

            while end-start+1 > k:
                curr_diff -= abs(arr[start]-x)
                start += 1

            size = end-start+1

            if size == k:
                if curr_diff < min_diff:
                    res_start, res_end = start, end
                    min_diff = min(min_diff, curr_diff)

            end += 1

        return arr[res_start:res_end+1]

        