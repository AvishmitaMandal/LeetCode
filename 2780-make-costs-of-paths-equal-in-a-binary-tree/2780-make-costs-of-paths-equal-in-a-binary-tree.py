class Solution:
    def minIncrementRecurse(self, curr, n, cost, inc):
        left = 2 * curr
        right = 2 * curr + 1
        # Leaf node
        if left > n and right > n:
            return cost[curr-1], inc

        if left <= n:
            left_sum, inc = self.minIncrementRecurse(left, n, cost, inc)
        if right <= n:
            right_sum, inc = self.minIncrementRecurse(right, n, cost, inc)

        inc += abs(left_sum - right_sum)
        node_sum = max(left_sum, right_sum) + cost[curr-1]

        return node_sum, inc


    def minIncrements(self, n: int, cost: List[int]) -> int:
        node_sum, inc = self.minIncrementRecurse(1, n, cost, 0)
        return inc