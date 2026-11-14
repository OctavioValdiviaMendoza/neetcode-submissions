# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Base case:
    
    if (p < root and q > root) or  (q < root and p > root):
        LCA -> root
        return LCA
    if p <= root or q <=root p.left == q or p.right == q:
        LCA -> min(p.val,q.val)
         LCA -> root
         return LCA
    if p >= root or q >=root p.left == q or p.right == q:
        LCA -> min(p.val,q.val)
        return LCA
    if p and q < root:
        LCA -> left-subtree
    if q and p > root:
        LCA -> right-subtree




'''

class Solution:
    LCA = None
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if self.LCA:
            return self.LCA
        if not root:
            return None

        if (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
            self.LCA = root
            return self.LCA
        if (root == p or root == q):
                self.LCA = root
                return self.LCA
            
        
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)

        

        return self.LCA

        
            
        
        
        