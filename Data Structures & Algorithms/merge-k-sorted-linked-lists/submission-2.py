# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, i, head))
        
        dummy = ListNode(0)
        curr = dummy

        while minHeap:
            val, index, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, index, node.next))
        
        return dummy.next