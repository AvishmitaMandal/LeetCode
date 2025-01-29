class Solution:
    def binary_search_start(self, list, target):
        start, end = 0, len(list)-1

        while start <= end:
            mid = (end + start) // 2
            if list[mid] <= target:
                start = mid+1

            else:
                end = mid-1
        
        return start

    def binary_search_end(self, list, target):
        start, end = 0, len(list)-1

        while start <= end:
            mid = (end + start) // 2
            if list[mid] < target:
                start = mid+1

            else:
                end = mid-1
        
        return start



    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_list, end_list = [], []
        for flower in flowers:
            start_list.append(flower[0])
            end_list.append(flower[1])

        start_list.sort()
        end_list.sort()

        print(start_list)
        print(end_list)

        res = []

        for p in people:
            flowers_start = self.binary_search_start(start_list, p)
            flowers_end = self.binary_search_end(end_list, p)
            res.append(flowers_start-flowers_end)

        return res
        