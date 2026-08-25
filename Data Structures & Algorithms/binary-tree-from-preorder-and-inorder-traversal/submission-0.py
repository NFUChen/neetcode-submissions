# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return
        # preorder = root first

        # preorder: [1, 2, 3, 4]
        # inorder: [2, 1, 3, 4]
        root_val = preorder[0]
        root_node = TreeNode(root_val)
        
        mid = inorder.index(root_val)

        root_node.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root_node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root_node

    


        