from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(source):
            if source in visited:
                return
            
            visited.add(source)

            for nei in graph[source]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        

        return res