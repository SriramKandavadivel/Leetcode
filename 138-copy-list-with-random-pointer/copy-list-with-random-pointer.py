"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if not head or not head.next:
        #     return head
        
        dummy = Node(0)
        
        vis = {}
        def rec(node):
            if not node:
                return None
            if node in vis:
                return vis[node]
            
            newNode = Node(node.val)
            vis[node] = newNode

            newNode.next = rec(node.next)
            newNode.random = rec(node.random)

            return newNode
        
        dummy.next = rec(head)
        return dummy.next