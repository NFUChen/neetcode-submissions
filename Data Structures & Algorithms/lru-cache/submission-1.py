class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache: dict[int, Node] = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    def _remove_node(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
    
    def _insert_node_at_right(self, node: Node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._insert_node_at_right(node)
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
        
        self.cache[key] = Node(key, value)
        self._insert_node_at_right(self.cache[key])


        if len(self.cache) > self.cap:
            # remove the lru
            lru = self.left.next
            self._remove_node(lru)
            del self.cache[lru.key]
        
