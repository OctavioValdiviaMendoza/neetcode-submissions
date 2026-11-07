# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
given a tree node we must recurse through the tree suing bfs and determine at each layer if the difference of heigts is more than 1.
we need to propagate the left and right height. or we can propagate a boolean if false we break the whole thing but if diff is or less we can prop true until we reach root again or condition is broken

dfs(curr):
    if not root:
        return 0
    left = dfs(curr.left)
    right = dfs(curr.right)

    self.height = abs(left - right)
    if self.height > 1:
        return False
    return 1 + max(left,right)

    return True


'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.height = abs(left - right)
            if self.height > 1:
                self.bal = False
            return 1 + max(left,right)
        dfs(root)

        return self.bal 
        
        