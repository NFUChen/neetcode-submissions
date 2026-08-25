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
        
        visited = dict()

        def dfs(node):
            if not node:
                return
            if node in visited:
                return visited[node]


            cp = Node(node.val)
            visited[node] = cp
            cp.next = dfs(node.next)
            cp.random = dfs(node.random)

            return cp
        
        return dfs(head)

