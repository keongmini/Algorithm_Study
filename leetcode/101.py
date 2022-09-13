# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        que_left = []
        que_right = []

        def left_(head, que):
            if not head:
                que.append(-1)
                return
            que.append(head.val)
            left_(head.left, que)
            left_(head.right, que)

        def right_(head, que):
            if not head:
                que.append(-1)
                return
            que.append(head.val)
            right_(head.right, que)
            right_(head.left, que)

        if not root or (not root.left and not root.right):
            return True

        left_(root.left, que_left)
        right_(root.right, que_right)

        if que_left == que_right:
            return True
        return False


