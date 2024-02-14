# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currNode = head

        #case of No Node in the linked-list
        if currNode==None:
            return None

        #case of One Node in the linked-list
        elif currNode.next==None:
            currNode = None
            return None

        #case of more than one node   
        n=0

        while currNode!=None:
            n+=1
            currNode = currNode.next

        mid = floor(n/2)

        currNode = prevNode = head
        n2 = 0

        while currNode!=None:
            if n2==mid:
                prevNode.next = currNode.next
                currNode.next = None 
                del currNode
                break
            n2 +=1
            prevNode = currNode
            currNode = currNode.next

        return head