# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            previous = head
            current = head.next
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            head.next=None
            return previous
        return head
        