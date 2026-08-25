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
        lookup = {None: None}

        curr = head
        while (curr):
            lookup[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while (curr):
            copy_node = lookup[curr]
            copy_node.next = lookup[curr.next]
            copy_node.random = lookup[curr.random]
            curr = curr.next
        

        return lookup[head]