# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        #edge cases
        #empty list
        if not head:
            return bool(0)
        
        #one node
        if not head.next:
            return bool(1)

        #save the values in a stack
        node = head
        stack = []
        while(node):
            stack.append(node.val)
            node = node.next

        #pop the first half of the list and save it in another list
        n = len(stack)

        #another edge case, if list is odd length, pop the middle value - don't need that, and compare the left and right half list
        if n%2==1:
            midPopped = stack.pop(int(n/2))

        stack2 = []
        for i in range(int(n/2)):
            pop = stack.pop()
            stack2.append(pop)

        #compare the two list and return 1/0
        return stack==stack2