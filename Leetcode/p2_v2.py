def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #first number
        num1 = ""
        while(l1):
            num1 = num1 + str(l1.val)
            l1 = l1.next

        num1 = num1[::-1]

        #second number
        num2 = ""
        while(l2):
            num2 = num2 + str(l2.val)
            l2 = l2.next

        num2 = num2[::-1]

        #sum
        sumnum = int(num1) + int(num2) 
        strnum = str(sumnum)

        #reverse linked list
        revnum = strnum[::-1]

        l3 = ListNode()
        l3_head = l3
        for i in range(0,len(revnum)):
            l3.val = revnum[i] #708
            if(i!=len(revnum)-1):
                l3.next = ListNode()
                l3 = l3.next

        l3 = l3_head

        return(l3)