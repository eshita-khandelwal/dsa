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
        store = {None:None}
        cur = head
        if head is None:
            return head
        while cur:
            newNode = Node(cur.val,None,None)
            store[cur] = newNode
            cur = cur.next
        
        for key,val in store.items():
            if key is None:
                continue
            val.next = store[key.next]
            val.random = store[key.random]

        return store[head]

                

