import heapq
class Solution:
    def jumpPossible(self, min_heap, jumps, mid, bricks, ladders):
        if len(min_heap) <= ladders:
            return True
        else:
            k = len(min_heap)-ladders
            jump_sum = 0
            while k:
                jump, start, end = heapq.heappop(min_heap)
                jump_sum += jump
                k -= 1
            if jump_sum <= bricks:
                return True
            return False

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        jumps = []

        for x in range(n-1):
            if heights[x] < heights[x+1]:
                # jumps = (height_diff, start, end)
                jumps.append((heights[x+1]-heights[x],x,x+1))

        ans1 = 0
        ans2 = len(heights)-1
        print(jumps)

        low, high = 0, len(jumps)-1
        while low <= high:
            mid = (low+high)//2

            # Form the heap
            min_heap = []
            for x in range(mid+1):
                heapq.heappush(min_heap, jumps[x])

            # Check if jump is possible
            jump, start, end = jumps[mid]
            if self.jumpPossible(min_heap, jumps, mid, bricks, ladders):
                ans1 = max(ans1, end)
                low = mid+1
            else: 
                ans2 = min(ans2, start)
                high = mid-1

        

        return max(ans1, ans2)

        