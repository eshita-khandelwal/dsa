# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            oddnex = even.next
            evennex = oddnex.next
            odd.next = oddnex
            odd = oddnex
            even.next = evennex
            even = evennex
        odd.next = evenHead
        return head
