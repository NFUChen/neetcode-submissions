
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def get_height(root) -> int:
            if root is None:
                return 0
            
            left = get_height(root.left)
            right = get_height(root.right)


            height_diff = max(left, right) - min(left, right)
            if height_diff > 1:
                self.is_balanced = False
                return 0
            
            return 1 + max(left, right)
        
        get_height(root)

        return self.is_balanced