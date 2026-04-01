class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev, curr = curr, max(curr, prev + nums[i])
        
        return curr