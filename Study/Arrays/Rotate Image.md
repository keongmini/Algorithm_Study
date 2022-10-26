# leetcode 48. [Rotate Image](https://leetcode.com/problems/rotate-image/) (medium)

* 문제 해설 : 행렬을 90도로 회전한 결과 출력, 새로운 값으로 출력하지 말고 in-place로 구현해야함
 
  example 1.
  ```text
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]
    ```
  <img src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" />
  
  example 2.
  ```text
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ```
  <img src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" />
  
  제약조건.
  ```text
    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
    ```
  
* Solution 풀이
  - 구현
  
    4개의 정사각형(최대 동일한 크기)을 90도로 돌려주는 방법  
    아래 그림을 예로 들면, (0,0), (0,1), (1,0), (1,1) 의 값을 90도로 회전했을 때의 위치에서 연쇄적으로 90도 회전해줌  
    <img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ff87ebee-9194-4ee0-842a-49075cdd08a0/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-10-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.56.53.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221026T115913Z&X-Amz-Expires=86400&X-Amz-Signature=1e83c2063c7fcce03a432499455838c4be34966e81a341963012aa52f1535397&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA%25202022-10-26%2520%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE%25208.56.53.png%22&x-id=GetObject" width='280'/>
    
    짝수의 경우, 정사각형을 90도로 회전해주면 전체 행렬이 90도로 회전되지만 홀수의 경우 최대크기의 정사각형을 구하고 나면 가로 세로 각 한줄씩 남음 해당 값 따로 처리  
    -> 반복문을 (n // 2 + n % 2) 돌려줌 - 홀수의 경우 한번 더 진행해야 하기 때문에 - 결국 직사각형 형태로 진행됨  
    <img src="https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e2718688-c5aa-4d08-bcec-02ecf518ba5e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-10-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.56.57.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221026%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221026T120300Z&X-Amz-Expires=86400&X-Amz-Signature=5b2ef841bf9f5a39d3753e804214f0d1acc8684f34376614ae96dd18969c63e7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA%25202022-10-26%2520%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE%25208.56.57.png%22&x-id=GetObject" width='280'/>
    
    **시간복잡도 O(N)**
  
    ```python
    class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            n = len(matrix[0])
            for i in range(n // 2 + n % 2):
                for j in range(n // 2):
                    tmp = matrix[n - 1 - j][i]
                    matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                    matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                    matrix[j][n - 1 - i] = matrix[i][j]
                    matrix[i][j] = tmp
    ```