"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return None

        if head in self.visitedHash:
            return self.visitedHash[head]

        node = Node(head.val)

        self.visitedHash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node