class Solution:
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)           # 트리 맨 밑에서 시작

            price_newpath = node.val + left_gain + right_gain       # 왼 + 노드 + 오른

            max_sum = max(max_sum, price_newpath)       # 모든 값 비교

            return node.val + max(left_gain, right_gain)        # 루트 노드로 갈 때는 왼, 오 중 하나

        max_sum = float('-inf')
        max_gain(root)

        return max_sum