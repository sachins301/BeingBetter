# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def rec(curr):
            count = -1
            if curr:
                count = rec(curr.next) + 1
            if count == n:
                temp = curr.next.next
                curr.next = temp
            return count
        dummyHead = ListNode()
        dummyHead.next = head
        c = dummyHead
        cnt = rec(c)
        return None if cnt == 0 else dummyHead.next