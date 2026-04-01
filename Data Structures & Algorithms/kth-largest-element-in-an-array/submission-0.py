class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        res = 0
        while k > 1:
            nums.pop()
            k -= 1
        res = nums.pop()
        return res
        
