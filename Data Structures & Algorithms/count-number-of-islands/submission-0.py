class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            if (r >= rows or c >= cols or grid[r][c] == "0" or 
                min(r, c) < 0):
                return
            
            grid[r][c] = '0'
            for newR, newC in directions:
                dfs(r + newR, c + newC)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands