class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        
        self.res = 0
        
        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0
            
            left_h = dfs(root.left)
            right_h = dfs(root.right)

            self.res = max(self.res, (left_h + right_h) )
            return 1 + max(left_h, right_h)
        
        dfs(root)

        return self.res