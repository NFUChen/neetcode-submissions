class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for _ in range(n)]
        parents = [i for i in range(n)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return 0
            
            if rank[px] > rank[py]:
                parents[py] = px
                rank[px] += rank[py]
            else:
                parents[px] = py
                rank[py] += rank[px]
            return 1
        

        res = n
        for u, v in edges:
            res -= union(u, v)
        
        return res