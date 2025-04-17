# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        second_p = None
        while second:
            tmp = second.next
            second.next = second_p
            second_p = second
            second = tmp
        
        first, second = head, second_p
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2