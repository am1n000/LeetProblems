# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        while n > 0:
            r = r.next
            n -= 1
        target = l
        while r:
            target = l
            l = l.next
            r = r.next
        if head == l:
            head = head.next
        target.next = l.next
        return head