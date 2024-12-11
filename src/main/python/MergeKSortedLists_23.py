from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1, l2):
            res = ListNode()
            curr = res
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return res.next

        if not lists:
            return

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(merge(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        res = ListNode(-1)
        res.next = lists[0]
        for node in lists[1:]:
            prev, curr = res, res.next
            curr2 = node
            while curr and curr2:
                if curr2.val < curr.val:
                    prev.next = curr2
                    tmp = curr2.next
                    curr2.next = curr
                    prev = curr2
                    curr2 = tmp
                else:
                    prev = curr
                    curr = curr.next

            if curr2:
                prev.next = curr2
        return res.next
