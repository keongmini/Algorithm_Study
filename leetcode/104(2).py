# level order

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()

        q.append((root, 1))

        result = 0

        if not root:
            return 0

        while q:
            now, depth = q.popleft()

            if now.left:
                q.append((now.left, depth + 1))

            if now.right:
                q.append((now.right, depth + 1))

            if not q:
                result = depth

        return result

# postorder

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1