class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, 2), (2, 1), (1, -2), (2, -1), 
                        (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
        
        x, y = abs(x), abs(y)
        que = deque([(0, 0, 0)])
        visit = {(0, 0)}

        while que:
            r, c, steps = que.popleft()
            if (r, c) == (x, y):
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr >= -2 and nc >= -2 and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    que.append((nr, nc, steps + 1))