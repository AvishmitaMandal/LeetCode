class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = {}
        total_tasks = len(tasks)
        
        for task in tasks:
            if task not in freq_dict:
                freq_dict[task] = 1
            else:
                freq_dict[task] += 1

        max_heap = []

        for key, val in freq_dict.items():
            max_heap.append(val)

        max_heap.sort(reverse = True)

        print(max_heap)

        max_freq = max_heap[0]
        idle_time = (max_freq - 1) * n
        print(idle_time)

        for x in range(1, len(max_heap)):
            curr_freq = max_heap[x]
            idle_time -= min(curr_freq, max_freq-1)
        
        if idle_time < 0:
            idle_time = 0
            
        return total_tasks + idle_time

        