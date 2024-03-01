class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None 
        curr = prev = head
        while(curr):
            if curr.val == val:
                if curr == head:
                    head = head.next
                    curr = prev = head
                else:
                    if curr.next:
                        prev.next = curr.next
                    else:
                        prev.next = None
                    curr = prev.next 
            else:
                prev = curr 
                curr = curr.next
        return head