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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
            Do not return anything, modify head in-place instead.
        """

        def helper(root, curr):
            if not curr:
                return root
            root = helper(root, curr.next)
            if not root:
                return None
            # print(root.val, curr.val)
            if root == curr or root.next == curr:
                curr.next = None
            else:
                tmp = root.next
                root.next = curr
                curr.next = tmp
            return curr.next

        helper(head, head.next)
        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find second half
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        # break the chain
        slow.next = None
        # reverse the second chain
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # join the chains
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1
        return head