from collections import defaultdict
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        mp_odd = defaultdict(int)
        mp_even = defaultdict(int)

        even_total, odd_total = 0, 0
        for x in range(len(nums)):
            if x % 2 == 0:
                mp_even[nums[x]] += 1
                even_total += 1
            else:
                mp_odd[nums[x]] += 1
                odd_total += 1

        odd_first_max_count, odd_first_max_ele = 0, -1
        even_first_max_count, even_first_max_ele = 0, -1
        odd_second_max_count, odd_second_max_ele = 0, -1
        even_second_max_count, even_second_max_ele = 0, -1

        # print(mp_even)

        for key, val in mp_even.items():
            if val > even_first_max_count:
                even_second_max_count = even_first_max_count
                even_second_max_ele = even_first_max_ele
                even_first_max_count = val
                even_first_max_ele = key
            elif val > even_second_max_count:
                even_second_max_count = val
                even_second_max_ele = key

        for key, val in mp_odd.items():
            if val > odd_first_max_count:
                odd_second_max_count = odd_first_max_count
                odd_second_max_ele = odd_first_max_ele
                odd_first_max_count = val
                odd_first_max_ele = key
            elif val > odd_second_max_count:
                odd_second_max_count = val
                odd_second_max_ele = key

        # print(even_total, odd_total)
        # print(odd_first_max_count, odd_first_max_ele)
        # print(even_first_max_count, even_first_max_ele)
        # print(odd_second_max_count, odd_second_max_ele)
        # print(even_second_max_count, even_second_max_ele)

        if even_first_max_ele != odd_first_max_ele:
            return (even_total - even_first_max_count) + (odd_total - odd_first_max_count)

        temp1 = (even_total - even_first_max_count) + (odd_total - odd_second_max_count)
        temp2 = (even_total - even_second_max_count) + (odd_total - odd_first_max_count)
        return min(temp1, temp2)

        