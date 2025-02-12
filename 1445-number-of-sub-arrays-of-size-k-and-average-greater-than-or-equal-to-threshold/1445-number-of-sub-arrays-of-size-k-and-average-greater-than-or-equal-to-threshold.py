class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        target = k * threshold

        start, end = 0, 0
        count = 0

        while end < len(arr):
            curr_sum += arr[end]

            while end - start + 1 > k:
                curr_sum -= arr[start]
                start += 1

            if end - start + 1 == k and curr_sum >= target:
                count += 1

            end += 1

        return count 
        