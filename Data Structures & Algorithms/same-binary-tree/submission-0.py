class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        traversal_p = []
        traversal_q = []

        def dfs(root, traversal: list[TreeNode]):
            if root is None:
                traversal.append(None)
                return
            
            traversal.append(root.val)
            dfs(root.left, traversal)
            dfs(root.right, traversal)
        

        dfs(p, traversal_p)
        dfs(q, traversal_q)

        return traversal_p == traversal_q