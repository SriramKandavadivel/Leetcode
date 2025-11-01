# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = ListNode(0)
        prev.next = head
        dummy.next = prev

        nums = set(nums)

        while head:
            if head.val in nums:
                prev.next = head.next
                head = head.next
                # prev = prev.next
            else:
                prev = prev.next
                head = head.next
        
        return dummy.next.next