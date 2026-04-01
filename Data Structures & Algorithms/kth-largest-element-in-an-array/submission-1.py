class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            minHeap.append(-num)
        heapq.heapify(minHeap)

        while k > 1:
            heapq.heappop(minHeap)
            k -= 1
        
        return -heapq.heappop(minHeap)