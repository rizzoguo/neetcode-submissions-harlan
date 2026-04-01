class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        l = 0
        res = []

        window.append(nums[0])
        for r in range(1,len(nums)):
            
            if r - l + 1 <= k:
                window.append(nums[r])
            
            else:
                curMax = max(window)
                res.append(curMax)
                window.pop(0)
                window.append(nums[r])
                
        res.append(max(window))
        return res
                