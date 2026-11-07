# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
input = Root node of a tree
ouput = int of diameter of a tree

diameter- the length of ht elongest path between any two nodes in a tree

One potential path is dfs from root node get max depth

can there be a case where we run bfs and not include the root and why woulnd't we include the root if it si a free point essenitally

so is this just simply a bfs search? get max depth of a bfs search, because it is a binary thee it means at most one node ahs two childrn but if we make a deep tree then we can have 


'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left+right)

            return 1 + max(left,right)
        dfs(root)
        return self.res

        