# leetcode 947. [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/) (medium)

* 문제 해설 : 주어진 값 중 같은 행 또는 열에 다른 값이 있을 경우 제거 가능, 제거될 수 있는 값의 개수 출력
 
  example 1. 
  ```text
    Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    Output: 5
    Explanation: One way to remove 5 stones is as follows:
    1. Remove stone [2,2] because it shares the same row as [2,1].
    2. Remove stone [2,1] because it shares the same column as [0,1].
    3. Remove stone [1,2] because it shares the same row as [1,0].
    4. Remove stone [1,0] because it shares the same column as [0,0].
    5. Remove stone [0,1] because it shares the same row as [0,0].
    Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
    ```
  
  example 2.
  ```text
    Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
    Output: 3
    Explanation: One way to make 3 moves is as follows:
    1. Remove stone [2,2] because it shares the same row as [2,0].
    2. Remove stone [2,0] because it shares the same column as [0,0].
    3. Remove stone [0,2] because it shares the same row as [0,0].
    Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
    ```
  
  example 3.
  ```text
    Input: stones = [[0,0]]
    Output: 0
    Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
    ```
  
  제약조건.
  ```text
    1 <= stones.length <= 1000
    0 <= xi, yi <= 104
    No two stones are at the same coordinate point.
    ```
  
* 문제 접근 방법

    행과 열을 기준으로 주어진 값을 정리한 후 주어진 값을 차례대로 탐색하며 행과 열에 값이 있을 경우 제거, 행과 열을 저장한 변수에서도 제거   
    다른 값과 행 또는 열로 연결이 되어있는 값이 먼저 제거되게 되면 제거 가능한 값도 제거되지 못하게 되어서 개수가 줄어듬  
    -> 연결된 행과 열의 개수를 확인하여 값이 적은 것부터 구현하는 방법을 생각했으나 이와 관계 없기 때문에 X
    
* Solution 풀이
  - DFS  
  참고. [discussion python solution](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/1689443/for-beginners-count-number-of-connected-graphs-o-n-94-faster/?orderBy=most_votes&languageTags=python)
  
      1. 행과 열을 기준으로 연결된 값 각각 저장
      2. 탐색 전인 값을 기준으로 dfs로 연결된 모든 값 탐색
      3. 2의 과정을 통해 분리 되어 있는 연결 개수 구하기(섬의 개수 처럼)
      4. 전체 길이에서 3에서 구한 개수 빼주기  
         각 구역별로 한개의 지점은 제거될 수 없음(이전에 연결된 값들이 모두 제거되었기 때문에)  
         따라서 구역의 개수를 구해서 전체 개수에서 빼주면 제거할 수 있는 개수가 됨
         
      **시간복잡도 O(N^2)**
      
      ```python
        class Solution:
            def removeStones(self, stones: List[List[int]]) -> int:
                def remove_point(a,b):
                    points.discard((a,b))
                    for y in x_dic[a]:
                        if (a,y) in points:
                            remove_point(a,y)
        
                    for x in y_dic[b]:
                        if (x,b) in points:
                            remove_point(x,b)
        
                x_dic = defaultdict(list)
                y_dic = defaultdict(list)
                points= {(i,j) for i,j in stones}
                
                for i,j in stones:
                    x_dic[i].append(j)
                    y_dic[j].append(i)
        
                cnt = 0
                for a,b in stones:
                    if (a,b) in points:
                        remove_point(a,b)
                        cnt+=1
        
                return len(stones)-cnt
    ```
   