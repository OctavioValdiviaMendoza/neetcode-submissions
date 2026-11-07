# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.equal = True
        def bfs_check(p,q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                self.equal = False
                return self.equal
            if p.val != q.val:
                self.equal = False
            bfs_check(p.left,q.left)
            bfs_check(p.right,q.right)

            return self.equal
        return bfs_check(p,q)
        