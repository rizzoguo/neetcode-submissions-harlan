class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        freqs = sorted(count.values())
        maxf = freqs[-1]
        idle = (maxf - 1) * n

        for freq in freqs[:-1]:
          temp = min(freq, maxf - 1)
          idle -= temp
        return len(tasks) + max(0, idle)