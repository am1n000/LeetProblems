"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        track = {}
        tmp_head = head

        while head:
            deep = Node(head.val)
            track[head] = deep
            head = head.next

        head = tmp_head
        while head:
            if head.next:
                track[head].next = track[head.next]
            if head.random:
                track[head].random = track[head.random]
            head = head.next
        
        return track[tmp_head]