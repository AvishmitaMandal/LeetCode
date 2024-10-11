class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        opt = []
        n = len(cost)

        for x in range(n):
            opt.append(0)

        opt[0] = cost[0]
        opt[1] = cost[1]
        for x in range(2,n):
            opt[x] = min(opt[x-1],opt[x-2]) + cost[x]

        return min(opt[n-1], opt[n-2])

        