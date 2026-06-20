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
        old_and_new_nodes = {}
        curr = head
        
        while curr:
            old_and_new_nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                old_and_new_nodes[curr].next = old_and_new_nodes[curr.next]
            
            if curr.random:
                old_and_new_nodes[curr].random = old_and_new_nodes[curr.random]
            
            curr = curr.next
        
        return old_and_new_nodes[head] if old_and_new_nodes else None