class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curList = []
        def dfs(i, total):
            if total == target:
                res.append(curList.copy())
                return
            
            if i == len(nums) or total > target:
                return 
            
            curList.append(nums[i])
            dfs(i, total + nums[i])
            curList.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res