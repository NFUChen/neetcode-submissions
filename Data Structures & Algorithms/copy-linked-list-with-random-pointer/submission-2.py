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
            _copy = Node(curr.val)
            lookup[curr] = _copy
            curr = curr.next
        
        curr = head
        while (curr):
            _copy = lookup[curr]
            _copy.next = lookup[curr.next]
            _copy.random = lookup[curr.random]
            curr = curr.next

        print(lookup)
        return lookup[head]