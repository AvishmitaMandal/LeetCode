import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)

        min_heap = []
        for x in range(n):
            if len(min_heap) != 0:
                top_end, top_interval = heapq.heappop(min_heap)
                if top_end > intervals[x][0]:
                    heapq.heappush(min_heap, (top_end, top_interval))

            heapq.heappush(min_heap,(intervals[x][1],intervals[x]))
    
        return len(min_heap)
            


        