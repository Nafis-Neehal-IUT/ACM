# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = -1
        counter = 0
        n = 0
        twoSum = 0
        currNode = head

        #counts n
        while(currNode):
            n += 1
            twoSum = twoSum + currNode.val 
            if currNode.next:
                currNode = currNode.next 
            else:
                if n==2:
                    return twoSum
                else:
                    break

        #assert n is even
        assert n%2==0 

        #calculate the midpoint/second half starting index [0-indexed]
        mid = n/2

        left = right = head 
        prev = head

        #offset right to mid point
        counter = 0
        while(left and right):
            
            if counter==0:
                temp = left.next
                left.next = None
                prev = left
                left = temp
            else:
                if counter < mid - 1 :
                    temp = left.next # 3 4 
                    left.next = prev # 1/head 2
                    prev = left # 2 3
                    left = temp # 2 3
                else:
                    right = left.next
                    left.next = prev
                    break

            counter += 1 

        #while right pointer doesn't hit the end of the linked list
        while(left and right):
            if left.val + right.val > maxSum:
                maxSum = left.val + right.val
            left = left.next
            right = right.next

        return maxSum

        