# leetcode 951. [Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/description/) (medium)

* 문제 해설 : 하위 자식 노드를 뒤집어서 두개의 트리를 동일하게 만들 수 있는지 여부 출력
 
  example 1. 
  ```text
    Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    Output: true
    Explanation: We flipped at nodes with values 1, 3, and 5.
    ```
  
  <img src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" />
  
  example 2.
  ```text
    Input: root1 = [], root2 = []
    Output: true
    ```
  
  example 3.
  ```text
    Input: root1 = [], root2 = [1]
    Output: false
    ```
  
  제약조건.
  ```text
    The number of nodes in each tree is in the range [0, 100].
    Each tree will have unique node values in the range [0, 99].
    ```
  
* Solution 풀이
  - 재귀
  
    1. 뒤집지 않아도 동일한 경우: roo1의 오른쪽 = root2의 오른쪽 and root1의 왼쪽 = root2의 왼쪽 
    2. 뒤집어서 동일한 경우: roo1의 오른쪽 = root2의 왼쪽 and root1의 왼쪽 = root2의 오른쪽
    
    재귀적으로 각 레벨별로 두 조건 검사 
    
    **시간복잡도 O(min(N, M)) N, M = root1, root2 길이**
    
    ```python
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    class Solution:
        def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 == root2:
                return True
            if not root1 or not root2 or root1.val != root2.val:
                return False
    
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) \
                   or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
    ```
  