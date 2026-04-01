class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        maxP = nums[0]

        for num in nums:
            temp = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, temp * num, curMin * num)
            maxP = max(maxP, curMax)
        return maxP