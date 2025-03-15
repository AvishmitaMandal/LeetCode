class Solution:
    '''
    [1,2,3,4,5,6,7,8,9,10]
    total = 55
    days = 10

    low = 8
    high = 9
    mid = 8

    req_days = 7
    weight_cap = 10

    '''
    def calculateDays(self, weights, mid):
        curr, res = 0, 0
        for weight in weights:
            if curr + weight <= mid:
                curr += weight
            else:
                curr = weight
                res += 1
                
        res += 1
        return res

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        low, high = max(weights), total
        weight_capacity = total + 1

        while low <= high:
            mid = (low + high)//2

            required_days = self.calculateDays(weights, mid)
            if required_days <= days:
                weight_capacity = min(weight_capacity, mid)
                high = mid - 1
            else:
                low = mid + 1

        return weight_capacity
        