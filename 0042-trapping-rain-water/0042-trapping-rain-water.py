class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        [0,1,0,2,1,0,1,3,2,1,2,1]
        left = [0,0,1,1,2,2,2,2,3,3,3,3]
        right = [3,3,3,3,3,3,3,2,2,2,1]
        '''

        water_unit = 0
        n = len(height)

        if n < 3:
            return 0
            
        left, right = [0] * n, [0] * n

        maxl = height[0]
        left[0] = maxl
        for x in range(1, n):
            maxl = max(maxl, height[x-1])
            left[x] = maxl


        maxr = height[n-1]
        right[0] = maxr
        for x in range(n-2, -1, -1):
            maxr = max(maxr, height[x+1])
            right[x] = maxr

        for x in range(n):
            if min(left[x], right[x]) - height[x] > 0:
                water_unit += min(left[x], right[x]) - height[x]

        return water_unit
        