# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)      # root에서 left로 연결되는 부분, right로 연결되는 부분 2개
            return max(left, right) + 1

        dfs(root)
        return self.longest


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0

        def dfs(node):
            nonlocal maxLength

            if not node:
                return 0

            leftLength = dfs(node.left)
            rightLength = dfs(node.right)

            maxLength = max(maxLength, leftLength + rightLength)

            return max(leftLength, rightLength) + 1

        dfs(root)
        return maxLength

# 풀이는 길이의 영역을 어디까지 보는지에 따라 달라짐