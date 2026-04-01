class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()

        for r, v in enumerate(nums):
            while window and nums[window[-1]] < v:
                window.pop()
            window.append(r)

            if window[0] <= r - k:
                window.popleft()
            
            if r + 1 >= k:
                res.append(nums[window[0]])
        
        return res

                