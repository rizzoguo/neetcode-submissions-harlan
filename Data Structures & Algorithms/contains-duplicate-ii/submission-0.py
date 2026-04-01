class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        intSet = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                intSet.remove(nums[l])
                l += 1
            if nums[r] in intSet:
                return True
            intSet.add(nums[r])
        
        return False