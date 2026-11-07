# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs_swap(node):
            if not node:
                return
            node.left,node.right = node.right, node.left
            dfs_swap(node.left)
            dfs_swap(node.right)
        dfs_swap(root)
        return root
        
            
        