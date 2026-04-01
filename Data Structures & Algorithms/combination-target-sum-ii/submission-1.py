class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curList, total):
            if total == target:
                res.append(curList.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curList.append(candidates[i])
            dfs(i + 1, curList, total + candidates[i])
            curList.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, curList, total)
        
        dfs(0, [], 0)
        return res