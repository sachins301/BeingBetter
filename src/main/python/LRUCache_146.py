class LinkedList:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastRecent = LinkedList(0, 0)
        self.mostRecent = LinkedList(0, 0)
        self.leastRecent.next, self.mostRecent.prev = self.mostRecent, self.leastRecent

    def insert(self, node):
        prev = self.mostRecent.prev
        prev.next = node
        node.next = self.mostRecent
        node.prev = prev
        self.mostRecent.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = LinkedList(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.leastRecent.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)