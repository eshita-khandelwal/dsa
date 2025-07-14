# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
       
        l, tail = 0, None
        cur = head
        
        while cur:
            tail = cur
            cur = cur.next
            l+=1
       
        k = k % l
        x = l-k-1
        if k == 0:
            return head
        nextt = None
        cur = head
        while cur and x:
            cur = cur.next
            nextt = cur
            x -=1

        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead
        

