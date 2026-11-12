# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Null subRoot is subTree of any tree
Tree is NUll and subRoot is not null -> False
If subroot not part of any subtree -> False

DFS -> Root , subRoot
    (Root.left -> Root.right ) == (subRoot)
    isSameTree:
        DFS traversal of both nodes (root, subRoot) -> True False
    

'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if (not root and subRoot) or (root and not subRoot):
                return False
            if root.val != subRoot.val:
                return False
            return (isSameTree(root.left, subRoot.left) and isSameTree(root.right,subRoot.right))

        
        if isSameTree(root, subRoot):
           return True
        

        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
            
        