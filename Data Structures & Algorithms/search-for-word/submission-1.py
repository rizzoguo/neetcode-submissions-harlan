class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c, curWord):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                (r, c) in visit):
                return False
            
            if board[r][c] != word[len(curWord)]:
                return False
                
            visit.add((r, c))
            curWord += board[r][c]
            if curWord == word:
                return True
            
            if (dfs(r + 1, c, curWord) or
                dfs(r, c + 1, curWord) or
                dfs(r - 1, c, curWord) or
                dfs(r, c - 1, curWord)):
                return True
            visit.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, ''):
                    return True
        
        return False
