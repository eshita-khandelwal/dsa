# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur!=None:
            nextNode = cur.next #2
            cur.next = prev #None
            prev = cur #1
            cur = nextNode #2

        head = prev

        return head 
