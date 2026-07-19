class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Fast & slow pointer concept
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

        #two-pass approach
        '''curr = head
        # First pass: count number of nodes
        l = 0
        while curr != None:
            curr = curr.next
            l += 1
        # Second pass: move l//2 steps from head
        curr = head
        for i in range(l // 2):
            curr = curr.next

        return curr'''
        

        