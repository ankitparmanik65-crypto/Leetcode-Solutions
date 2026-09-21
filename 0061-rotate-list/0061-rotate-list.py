# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        # Step 1: find length and last node
        curr = head
        n = 1
        while curr.next is not None:
            curr = curr.next
            n += 1

        # Step 2: reduce k
        k = k % n
        if k == 0:
            return head

        # Step 3: make list circular
        curr.next = head

        # Step 4: find new tail (n - k - 1 steps from head)
        steps_to_new_tail = n - k
        new_tail = head
        for i in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 5: new head is next of new tail
        new_head = new_tail.next

        # Step 6: break the circle
        new_tail.next = None

        return new_head