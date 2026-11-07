# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
input = tree node
output = int -> longest path between two nodes = diameter 
                 could include root could not

we need to calculate the diameter at every stage  but we also need to pass the largest height
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def bfs(curr):
            if not curr:
                return 0
            left = bfs(curr.left)
            right = bfs(curr.right)

            self.res = max(self.res, left+right)

            return 1 + max(left,right)
        bfs(root)

        return self.res

        