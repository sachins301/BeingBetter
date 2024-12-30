# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not slow or not fast or not fast.next:
            return None
        slow2 = head
        pos = 0
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
            pos += 1
        return slow