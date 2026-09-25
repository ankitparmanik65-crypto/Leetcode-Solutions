# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy

        curr1 = l1
        curr2 = l2
        c = 0

        while curr1 != None or curr2 != None or c != 0:
            total = c
            c = 0

            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next

            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next

            if total > 9:
                c = 1
                total -= 10

            result.next = ListNode(total)
            result = result.next

        return dummy.next
        