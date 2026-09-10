"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if len(node.neighbors) == 0:
            return Node(node.val)
        
        old_to_new = dict()
        '''
        create a mapping from oldNode to newNode
        key-> old Node value -> New Created Node
        '''
        old_to_new[node] = Node(node.val)

        def dfs_node_construction(node1):
            for neighbor in node1.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    dfs_node_construction(neighbor)
                old_to_new[node1].neighbors.append(old_to_new[neighbor])
        
        dfs_node_construction(node)
        
        return old_to_new[node]


                    




        