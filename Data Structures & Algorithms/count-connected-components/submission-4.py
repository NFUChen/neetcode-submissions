class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parents = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])

            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)

            # same parent, no need to union
            if px == py:
                return 0
            
            if rank[px] > rank[py]:
                parents[py] = px
                rank[px] += 1
            else:
                parents[px] = py
                rank[py] += 1
            
            return 1
        res = n
        for u, v in edges:
            res -= union(u, v)
        
        return res