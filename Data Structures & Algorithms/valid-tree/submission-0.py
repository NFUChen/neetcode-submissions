class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
        
        seen = set()

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            seen.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(seen) == n