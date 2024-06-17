// Solution 풀이
class Solution {
    val directions = arrayOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)      // [(1, 0), (-1, 0), (0, 1), (0, -1)]

    fun numIslands(grid: Array<CharArray>): Int {
        var count = 0

        for (i in 0..<grid.size){              // 끝 숫자 확인 x
            for (j in 0..<grid[0].size){
                if(grid[i][j] == '1'){          // "1" => String, '1' => Char 구분 필요
                    count ++
                    bfs(grid, i, j)
                }
            }
        }

        return count
    }

    fun bfs(grid:Array<CharArray>, row:Int, col:Int) {
        val q:Queue<Pair<Int, Int>> = LinkedList<Pair<Int, Int>>()

        q.add(Pair(row, col))

        while (q.isNotEmpty()){
            val (r, c) = q.remove()

            for((dx, dy) in directions){
                val nr = r + dx
                val nc = c + dy

                if(nr < 0 || nc < 0 || nr >= grid.size || nc >= grid[0].size || grid[nr][nc] == '0'){
                    continue
                }

                q.add(Pair(nr, nc))
                grid[nr][nc] = '0'
            }
        }
    }
}
