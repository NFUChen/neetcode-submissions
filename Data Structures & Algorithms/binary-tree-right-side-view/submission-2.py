# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = [root]
        while (queue):
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                    level.append(node.val)
            if len(level) != 0:
                res.append(level[-1])
        
        return res
        
                