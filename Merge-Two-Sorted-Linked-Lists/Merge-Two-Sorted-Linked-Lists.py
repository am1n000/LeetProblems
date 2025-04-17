# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = list1
        if list1.val > list2.val:
            head = list2

        tmp = list2
        while list1 and list2:
            if list2.val < list1.val:
                if tmp != list2:
                    tmp.next = list2
                while list2 and list2.val <= list1.val:
                    tmp = list2
                    list2 = list2.next
                tmp.next = list1
            tmp = list1
            list1 = list1.next
        if list2:
            tmp.next = list2
        return head
