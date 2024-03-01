# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap = {}
        na = headA
        nb = headB
        while na:
            if na in hashmap.keys():
                return na
            else:
                hashmap.update({na:1})
            na = na.next
        
        while nb:
            if nb in hashmap.keys():
                return nb
            else:
                hashmap.update({nb:1})
            nb = nb.next
        