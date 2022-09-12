# 내풀이 - 실패 (Wrong answer)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def binary_search(head, pivot, d):

            if not head.left and not head.right:
                return True

            if d == '-':
                if head.left and head.left.val >= head.val:
                    return False
                if head.right:
                    if head.right.val <= head.val or head.right.val >= pivot:
                        return False

            if d == '+':
                if head.left:
                    if head.left.val >= head.val or head.left.val <= pivot:
                        return False
                if head.right and head.right.val <= head.val:
                    return False

            left = binary_search(head.left, pivot, d) if head.left else True
            right = binary_search(head.right, pivot, d) if head.right else True

            return left and right

        left = right = False

        if not root.left:
            left = True
        if not root.right:
            right = True
        if root.left and root.left.val < root.val:
            left = binary_search(root.left, root.val, '-')
        if root.right and root.right.val > root.val:
            right = binary_search(root.right, root.val, '+')

        return left and right

# leetocde solution
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)