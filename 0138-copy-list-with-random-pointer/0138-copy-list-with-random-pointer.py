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
        #hashMap is used for mapping the new node to old node
        hashMap = {None:None}
        cur = head
        
        while cur:
            hashMap[cur] = Node(cur.val,None)
            cur = cur.next
        
        cur = head
        while cur:
            hashMap[cur].next = hashMap[cur.next]
            hashMap[cur].random = hashMap[cur.random]
            cur = cur.next
        return hashMap[head]