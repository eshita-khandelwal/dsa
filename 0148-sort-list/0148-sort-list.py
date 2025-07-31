# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self,head):
        slow,fast = None,head
        
        while fast and fast.next:
            slow  = head if not slow else slow.next
            fast=fast.next.next
        mid = slow.next
        slow.next = None
        return mid
            
    def merge(self,left,right):
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #for sorting the linked list merge sort is used. O(nlogn)
        if not head or not head.next:
            return head

        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)
    

