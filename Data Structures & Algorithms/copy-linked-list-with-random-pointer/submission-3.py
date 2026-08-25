class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        visited = {}

        def dfs(node):
            if not node:
                return None

            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy

            copy.next = dfs(node.next)
            copy.random = dfs(node.random)

            return copy

        return dfs(head)