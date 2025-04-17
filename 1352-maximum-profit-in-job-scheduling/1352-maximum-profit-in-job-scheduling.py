class Solution:
    def isOverlap(self, curr_job, next_job):
        return curr_job[1] > next_job[0]

    def nextAvailableJob(self, startTime, target):
        ans = len(startTime)
        low, high = 0, len(startTime)-1
        
        while low <= high:
            mid = (low+high)//2
            if startTime[mid] >= target:
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

    def jobSchedulingRecurse(self, job_info, i, dp, startTime):
        if i >= len(job_info):
            return 0

        idx = self.nextAvailableJob(startTime, job_info[i][1])
        if idx == len(job_info):
            selecting = job_info[i][2]
        elif dp[idx] != -1:
            selecting = job_info[i][2] + dp[idx]
        else:
            dp[idx] = self.jobSchedulingRecurse(job_info, idx, dp, startTime)
            selecting = job_info[i][2] + dp[idx]

        if i+1 >= len(job_info):
            not_selecting = 0
        elif dp[i+1] != -1:
            not_selecting = dp[i+1]
        else:
            dp[i+1] = self.jobSchedulingRecurse(job_info, i+1, dp, startTime)
            not_selecting = dp[i+1]

        profit = max(selecting, not_selecting)

        dp[i] = profit
        return profit

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        job_info = []
        n = len(startTime)

        for x in range(n):
            job_info.append([startTime[x], endTime[x], profit[x]])
        job_info.sort()
        dp = [-1] * n

        profit = 0
        startTime.sort()
        max_profit = self.jobSchedulingRecurse(job_info, 0, dp, startTime)

        return max_profit
        
        