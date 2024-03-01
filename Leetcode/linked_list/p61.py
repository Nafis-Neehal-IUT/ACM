# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #special cases
        if not head:
            return None
        if not head.next:
            return head

        #count the length of a linked list
        node = head
        count = 0
        end = None

        while(node):
            if node.next==None:
                end = node
            node = node.next
            count += 1
        
        #mod the k by length
        headShift = k % count

        #shift right headShift amount of times instead of k times, max_k = len(linked_list)
        start = ListNode()
        end = head
        while(headShift):
            while(end.next):
                start = end
                end = end.next
            end.next = head #5->1
            start.next = None #4->*/
            head = end #5
            headShift -=1

        return head
        
        # def buildHashmap(numStr, k): #easier to string
        #     hashmap = {0:numStr}
        #     for i in range(1, len(numStr)):
        #         newStr = numStr[-1] + numStr[:-1]
        #         hashmap[i] = newStr
        #         numStr = newStr
        #     return(hashmap[k%len(numStr)])

        # s = ''
        # node=head
        # while(node):
        #     s = s + str(node.val)
        #     node = node.next
        
        # combination = buildHashmap(s, k)
        
        # node=head
        # i = 0
        # while(node):
        #     node.val = combination[i]
        #     node = node.next
        #     i +=1
        
        # return head
