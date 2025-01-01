class Solution:
    def isOverlap(self, prev, curr):
        if prev[1] >= curr[0]:
            return True
        return False

    def mergedInterval(self, prev, curr):
        interval = []
        interval.append(min(prev[0], curr[0]))
        interval.append(max(prev[1], curr[1]))
        return interval
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
        [[1,3],[2,6],[8,10],[15,18]]
        '''

        sorted_intervals = sorted(intervals)
        result = []

        prev_interval = sorted_intervals[0]
        is_overlap = 0

        for x in range(1, len(sorted_intervals)):
            curr_interval = sorted_intervals[x]
            is_overlap = self.isOverlap(prev_interval, curr_interval)
            if is_overlap:
                merged_interval = self.mergedInterval(prev_interval, curr_interval)
                prev_interval = merged_interval
            else:
                result.append(prev_interval)
                prev_interval = curr_interval

     
        result.append(prev_interval)

        return result

        


        
        