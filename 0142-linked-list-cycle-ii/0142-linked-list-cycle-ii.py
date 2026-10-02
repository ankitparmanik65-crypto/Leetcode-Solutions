# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Phase 1: detect cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Phase 2: find the start of the cycle
                slow2 = head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow2

        return None        