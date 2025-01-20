import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for word in words:
            if word not in frequency:
                frequency[word] = 1
            else:
                frequency[word] += 1

        heap = []
        for word, val in frequency.items():
            heapq.heappush(heap, (-1*val, word))

        result = []
        print (heap)
        while k:
            (val, word) = heapq.heappop(heap) 
            result.append(word)
            k -= 1

        return result

        