
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            nodeMap[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = nodeMap[curr]
            copy.next = nodeMap.get(curr.next, None)
            copy.random = nodeMap.get(curr.random, None)
            curr = curr.next

        return nodeMap.get(head, None)

