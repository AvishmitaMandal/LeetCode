from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(timestamp)
        pack = zip(username, timestamp, website)
        sorted_pack = sorted(pack, key = lambda x: x[1])
        # print(sorted_pack)

        mp_user_visit = defaultdict(list)
        for x in range(n):
            user, time, site = sorted_pack[x]
            mp_user_visit[user].append(site)

        print(mp_user_visit)

        mp_pattern = defaultdict(int)

        for key, val in mp_user_visit.items():
            word_list = val
            size = len(word_list)
            if size < 3:
                continue
            visited = set()
            for x in range(0,size-2):
                for y in range(x+1, size-1):
                    for z in range(y+1, size):
                        seq = (word_list[x], word_list[y], word_list[z])
                        if seq not in visited:
                            mp_pattern[seq] += 1
                        visited.add(seq)
        
        # print(mp_pattern)

        pattern, count = [], 0
        for key, val in mp_pattern.items():
            if val >= count:
                if val == count and key > pattern:
                    continue
                else:
                    pattern = key
                    count = val

        return list(pattern)
            
        