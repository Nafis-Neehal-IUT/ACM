# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return bool(0)
        if not head.next:
            return bool(0)
        listnodes = set()
        node = head
        while(node):
            if node in listnodes:
                return bool(1)
            listnodes.add(node)
            node = node.next
        return bool(0)
        
        