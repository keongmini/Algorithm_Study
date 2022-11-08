# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) \
               or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

    # (root1 오른쪽 = root2 오른쪽) + (root1 왼쪽 = root2 왼쪽)
    # (root1 오른쪽 = root2 왼쪽) + (root1 왼쪽 = root2 오른쪽)
    # 둘 중 하나여야 함