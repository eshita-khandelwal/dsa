class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = self.right = Node(0,0) #dummy nodes 
        #initially we would want these nodes to be connected to each other
        self.left.next = self.right #left is least recent
        self.right.prev = self.left #right is most recent

    #whenever we are removing in our code it will always be the middle node
    def remove(self,node):  
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev
    
    #insert at the right as the most recent element
    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next=nxt.prev = node
        node.next,node.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            print(self.cache[key].val)
            self.remove(self.cache[key])
            self.insert(self.cache[key]) #most recent used that is why insert again
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)