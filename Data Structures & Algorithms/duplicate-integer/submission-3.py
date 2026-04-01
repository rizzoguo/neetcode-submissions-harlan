class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for num in nums:
            check.add(num)
        
        return True if len(check) != len(nums) else False
