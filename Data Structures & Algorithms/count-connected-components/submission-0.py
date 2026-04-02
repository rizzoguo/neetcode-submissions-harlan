class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        component = 0
        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
        
        for node in range(n):
            if node not in visit:
                component += 1
                dfs(node)
        return component
            