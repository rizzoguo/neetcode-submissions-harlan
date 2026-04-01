class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        res = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(heap, (distance, point))
        
        while k > 0:
            
            distance, point = heapq.heappop(heap)
            res.append(point)
            k -= 1
        
        return res
