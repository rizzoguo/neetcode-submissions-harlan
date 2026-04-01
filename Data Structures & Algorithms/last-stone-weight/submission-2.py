class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
          stoneX = heapq.heappop(heap)
          stoneY = heapq.heappop(heap)
          if stoneX < stoneY:
            heapq.heappush(heap, stoneX - stoneY)
      
        return -heap[0] if heap else 0