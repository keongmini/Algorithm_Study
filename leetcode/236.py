class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(root, p, q):
            if root == None:
                return None

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)

            if root == p or root == q:          # 현재 내가 대상 값 중 하나 인 경우
                return root

            elif left and right:                # 둘다 값이 있는 경우 - 내가 조상인 경우
                return root

            return left or right                # 둘 중 하나라고 None이거나 둘다 Nonde인 경우

        return LCA(root, p, q)


s = Solution()
result = s.lowestCommonAncestor([3,5,1,6,2,0,8,None,None,7,4], 5, 1)
print(result)