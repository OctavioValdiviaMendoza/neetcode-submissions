# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Recursive: Propagate the value to the top

#1 check if they are both tree node objects
    #1.1 if they are not  tree Node objects (NONE) return true becasue they are the same 
    #1.2 if they are check if they are the same value
#2 Check if one is none and Treenode -> False 

"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if  p.val != q.val:
            return False
        
        
        if not self.isSameTree(p.left, q.left):
            return False
        if not self.isSameTree(p.right, q.right):
            return False   
        
        return True
        


        
        