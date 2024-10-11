'''
0   1   2   3   4  
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        steps = []
        for x in range(n+1):
            steps.append(1)
        
        for x in range(2,n+1):
            steps[x] = steps[x-1] + steps[x-2]

        return steps[n]

        