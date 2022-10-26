# leetcode 297. [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (hard)

* 문제 해설 : tree -> str, str -> tree 로 바꾸는 것 두가지 구현 (값이 없는 경우 str에 아무것도 아닌 값 넣어줘야 함)
  <img src="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/Figures/297_BST.png" />
 
  예시는 deserialize 된 경우  
  example 1. 
  ```text
    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]
  ```
  
  example 2.
  ```text
    Input: root = []
    Output: []
  ```
  
  제약조건.
  ```text
    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000
  ```
  
* Solution 풀이
  - bfs
    
    * seriarlize : 노드의 left, right를 dq에 저장, 값이 없을 경우 None으로 연결 
    * deserialize : ','를 기준으로 split 해서 레벨별로 연결
    
    **시간복잡도 O(N)**
    
    ```python
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    import collections
    class Codec:
    
        def serialize(self, root):
            if not root:
                return ''
            
            q = collections.deque()
            q.append(root)
            result = ''
            while q:
                node = q.popleft()
                if not node:
                    result += 'None,'
                    continue
                result += str(node.val) + ','
                q.append(node.left)
                q.append(node.right)
                
            return result 
            
        def deserialize(self, data):
            if not data:
                return None
            ls = data.split(',')
            root = TreeNode(int(ls[0]))
            q = collections.deque()
            q.append(root)
            i = 1
            while q and i < len(ls):
                node = q.popleft()
                if ls[i] != 'None':
                    left = TreeNode(int(ls[i]))
                    node.left = left
                    q.append(left)
                i += 1
                if ls[i] != 'None':
                    right = TreeNode(int(ls[i]))
                    node.right = right
                    q.append(right)
                i += 1
            return root
    ```
    
  - dfs
    
    * serialize : root 노드를 기준으로 left, right으로 계속 재귀 -> left 결과에 right 결과 연결  
    * deserialize : serialize와 동일한 방식으로 진행
    
    **시간복잡도 O(N)**
    
    ```python
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    import collections
    class Codec:
    
        def serialize(self, root):
            def rserialize(root, string):
                if root is None:
                    string += 'None,'
                else:
                    string += str(root.val) + ','
                    string = rserialize(root.left, string)
                    string = rserialize(root.right, string)
                return string
            
            return rserialize(root, '')
            
        def deserialize(self, data):
            def rdeserialize(l):
                if l[0] == 'None':
                    l.pop(0)
                    return None
                    
                root = TreeNode(l[0])
                l.pop(0)
                root.left = rdeserialize(l)
                root.right = rdeserialize(l)
                return root
    
            data_list = data.split(',')
            root = rdeserialize(data_list)
            return root
    ```
    
> serialize의 경우 bfs와 dfs의 출력되는 값이 다름 -> 상관x, 연결성만 보여주면 됨