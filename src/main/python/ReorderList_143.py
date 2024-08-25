# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ReorderList_143:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def rec(currHead, curr):
            if curr.next:
                currHead = rec(currHead, curr.next)
            # print(currHead, curr)
            if currHead and currHead.next == curr or currHead == curr:
                curr.next = None
            elif currHead:
                temp = currHead.next
                currHead.next = curr
                curr.next = temp
                # print(currHead)
                return temp
            return
        ch = head
        c = head
        ch = rec(ch, c)
        seen = set()
        while(c):
            if c in seen:
                break
            seen.add(c)
            # print(c.val)
            c = c.next
        return