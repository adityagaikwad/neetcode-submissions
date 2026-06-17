'''
Brute force will be use a list and do list.pop(i) to remove old cache
where we append((key, value)) to list
O(n) for both
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # We will use a doubly linked list
        # with left pointing to oldest element
        # and right pointing to most recent element
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        # add the double sided pointers
        self.left.next = self.right
        self.right.prev = self.left

        # maintain a hashmap for key -> node ref
        self.cache = {}

    def remove(self, node):
        # get prev and next of node
        prev = node.prev
        next = node.next
        # add links between prev and next nodes
        prev.next = next
        next.prev = prev

    def insert(self, node):
        # self.right is a dummy node
        # self.right.prev is the last actual node
        prev_node = self.right.prev
        # form links with prev_node
        prev_node.next = node
        node.prev = prev_node
        # form links with self.right
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(self.left.next)
            del self.cache[lru.key]


