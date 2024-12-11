# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        groupprev = res

        while True:
            count = 0
            kth = groupprev
            while kth and count < k:
                count += 1
                kth = kth.next
            if not kth:
                break
            groupnext = kth.next

            prev, curr = kth.next, groupprev.next
            while curr != groupnext:
                print(prev.val, curr.val, kth.next.val, groupnext.val)
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                print('at end', prev.val, curr.val, kth.next.val, groupnext.val)
            print('okay im out')
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp
        return res.next

