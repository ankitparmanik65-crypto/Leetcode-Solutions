# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev_critical = -1
        min_dist = float('inf')
        index = 1

        prev = head
        curr = head.next

        while curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - prev_critical)

                prev_critical = index

            prev = curr
            curr = curr.next
            index += 1

        if first == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]        