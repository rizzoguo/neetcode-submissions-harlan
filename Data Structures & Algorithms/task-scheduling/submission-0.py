class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxFreq = sorted(count.values())
        idle = (maxFreq[-1] - 1) * n

        for freq in maxFreq[:-1]:
            temp = min(maxFreq[-1] - 1, freq)
            idle -= temp
        
        return len(tasks) + max(idle, 0)