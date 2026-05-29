# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = None
        previous = None
        while p1 or p2:
            v1 = p1.val if p1 else 200
            v2 = p2.val if p2 else 200
            if v1 <= v2:
                current = ListNode(v1)
                p1 = p1.next
            else:
                current = ListNode(v2)
                p2 = p2.next
            if not head:
                head = current
                previous = current
            else:
                previous.next = current
                previous = current
            
        return head