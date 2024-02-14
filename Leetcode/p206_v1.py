# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return None 
        if head.next==None:
            return head
        
        curr = prev = head
        while(curr):
            if curr==head:
                temp = head.next
                head.next = None
                prev = curr 
                curr = temp
            else:
                if curr.next: #still one node left
                    temp = curr.next 
                    curr.next = prev 
                    prev = curr 
                    curr = temp
                else:
                     curr.next = prev
                     return curr
        