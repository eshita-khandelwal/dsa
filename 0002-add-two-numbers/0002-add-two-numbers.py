# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0,None)
        res = result
        s,c =0,0
        while l1 and l2:
            s = (l1.val + l2.val + c) % 10
            res.next = ListNode(s,None)
            print(res)
            c = (l1.val + l2.val + c) //10
            l1 = l1.next
            l2 = l2.next
            res = res.next
        while l1:
            s = (l1.val + c) %10
            res.next = ListNode(s,None)
            c = (l1.val + c) //10
            l1 = l1.next
            res = res.next
            
        while l2:
            s = (l2.val + c) % 10
            res.next = ListNode(s,None)
            c = (l2.val + c) //10
            l2 = l2.next
            res = res.next
            
        if c!=0:
            newNode = ListNode(c,None)
            res.next = newNode
        return result.next


