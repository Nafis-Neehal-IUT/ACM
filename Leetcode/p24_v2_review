
#solution with list
#borrowed from Lalithkiran
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        ans=[]
        for i in range(0,len(lst),2):
            val=lst[i:i+2]
            ans+=val[::-1]
        final=ListNode(0)
        tmp=final
        for i in ans:
            tmp.next=ListNode(i)
            tmp=tmp.next
        return final.next

#my attempt with linked list
def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 
        if head.next==None:
            return head
        
        left = head
        right = head.next
        counter = 0
        while(left and right):
            left.next = right.next
            right.next = left
            left = left.next
            if counter == 0:
                head = right
            if left:
                right = left.next
            else:
                right = None
            counter += 2
        return head