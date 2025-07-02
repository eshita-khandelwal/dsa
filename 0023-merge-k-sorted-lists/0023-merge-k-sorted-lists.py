# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        count = {}
        for i in range(len(lists)):
            list2 = lists[i]
            h = list2
            while h:
                count[h.val] = 1 + count.get(h.val,0)
                h = h.next
        count = dict(sorted(count.items()))
        
        result = ListNode(0,None)
        res = result
        
        for key,val in count.items():
            while count[key]:
                res.next = ListNode(key,None)
                res = res.next
                count[key] -=1
        return result.next