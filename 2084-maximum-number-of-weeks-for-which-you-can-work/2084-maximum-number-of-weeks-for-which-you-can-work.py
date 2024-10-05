class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total_task = 0
        for milestone in milestones:
            total_task += milestone

        milestones.sort(reverse = True)
        max_freq = milestones[0]

        idle_time = max_freq-1

        for x in range(1, len(milestones)):
            idle_time -= min(max_freq-1, milestones[x])

        if idle_time <= 0:
            return total_task

        else:
            return total_task-idle_time 
        