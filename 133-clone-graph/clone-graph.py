"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        vis = {}
        def clone(node):
            if node in vis:
                return vis[node]
            node_c = Node(node.val,[])  #new node
            vis[node] = node_c

            for neigh in node.neighbors:
                node_c.neighbors.append(clone(neigh))
            return node_c 
        return clone(node)