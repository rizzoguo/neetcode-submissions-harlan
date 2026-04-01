class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
          distance = point[0]**2 + point[1]**2
          minHeap.append((distance, point))
        heapq.heapify(minHeap)

        res = []
        while k > 0:
          distance, point = heapq.heappop(minHeap)
          res.append(point)
          k -= 1
          
        return res