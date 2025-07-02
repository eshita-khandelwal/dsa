# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        h = head
        while h:
            h = h.next
            l +=1
        r = l - n
        
        curr = head
        prev = None
        if r == 0:
            return head.next
            
        while curr and r:
            prev = curr
            curr = curr.next
            print(prev.val,curr.val)
            r -=1
        if prev == None:
            return prev
        else:
            prev.next = curr.next
        return head
        