class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection
        slow = nums[0]
        fast = nums[0]

        # Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find entrance of cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow        