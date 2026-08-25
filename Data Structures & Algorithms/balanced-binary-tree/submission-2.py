
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.is_bal = True

        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)


            diff = max(left, right) - min(left, right)
            if diff > 1:
                self.is_bal = False
                return 0



            

            return 1 + max(left, right)
        dfs(root)
        return self.is_bal 