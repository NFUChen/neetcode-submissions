# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, max_so_far):
            if not root:
                return
            
            
            
            new_max = max(max_so_far, root.val)

            if root.val >= new_max:
                nonlocal res
                res += 1

            dfs(root.left, new_max)
            dfs(root.right, new_max)

        dfs(root, float("-inf"))

        return res