# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
input: TreeNode -> root
output: List of list of each layer of the tree

q -> deque

answer = []
BFS -> each layer of BFS:
        current_layer = []
        append left and right child to deque
        pop the queue I wold to add list
        end of the layer append the 
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        answer = [[root.val]]
        print(answer)
        while q:  
            current_layer = [] 
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    current_layer.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    current_layer.append(node.right.val)
            if len(current_layer) != 0:
                answer.append(current_layer)
            
        return answer



        