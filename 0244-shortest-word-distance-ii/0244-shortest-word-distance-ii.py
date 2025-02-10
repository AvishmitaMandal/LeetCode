from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.mp = defaultdict(list)
        for x in range(len(wordsDict)):
            self.mp[wordsDict[x]].append(x)

    def shortest(self, word1: str, word2: str) -> int:
        word1_list, word2_list = self.mp[word1], self.mp[word2]
        first, second = 0,0

        print(word1_list)
        print(word2_list)

        shortest_dist = max(max(word1_list), max(word2_list))

        while first < len(word1_list) and second < len(word2_list):
            shortest_dist = min(shortest_dist, abs(word1_list[first]-word2_list[second]))
            if first+1 < len(word1_list) and second + 1 < len(word2_list):
                if abs(word1_list[first+1]-word2_list[second]) < abs(word1_list[first]-word2_list[second+1]):
                    first += 1
                else:
                    second += 1
            else:
                break
            
        while first < len(word1_list):
            if first+1 < len(word1_list) and shortest_dist > abs(word1_list[first+1]-word2_list[second]):
                first += 1
                shortest_dist = abs(word1_list[first]-word2_list[second])
            else:
                break

        while second < len(word2_list):
            if second+1 < len(word2_list) and shortest_dist > abs(word1_list[first]-word2_list[second+1]):
                second += 1
                shortest_dist = abs(word1_list[first]-word2_list[second])
            else:
                break

        return shortest_dist

        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)