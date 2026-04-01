class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []
        for stone in stones:
            self.heap.append(-stone)
        heapq.heapify(self.heap)

        while len(self.heap) >= 2:
            stoneX = heapq.heappop(self.heap)
            stoneY = self.heap[0]
            if stoneX == stoneY:
                heapq.heappop(self.heap)
            else:
                stoneY = heapq.heappop(self.heap)
                heapq.heappush(self.heap, stoneX - stoneY)
                heapq.heapify(self.heap)
        
        if not self.heap:
            return 0
        else:
            return abs(self.heap[0])
        
        
        