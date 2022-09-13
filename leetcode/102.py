# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def tree(head, result, level):
            if not head:
                return

            result[level].append(head.val)

            tree(head.left, result, level + 1)
            tree(head.right, result, level + 1)

        result = collections.defaultdict(list)
        tree(root, result, 0)

        answer = []
        for i in result.values():
            answer.append(i)

        return answer