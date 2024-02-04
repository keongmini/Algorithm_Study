class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        val result = mutableListOf<Int>()
        var x = 0
        var y = 0
        var n = matrix.size - 1
        var m = matrix[0].size - 1
        var d = 0
        while (x <= n && y <= m) {
            if (d == 0) {
                for (i in y until m + 1) {      // until -> 끝 숫자는 포함되지 않음
                    result.add(matrix[y][i])
                }
                x++
            } else if (d == 1) {
                for (i in x until n + 1) {
                    result.add(matrix[i][m])
                }
                m--
            } else if (d == 2) {
                for (i in m downTo y) {     // downTo -> 양쪽 포함
                    result.add(matrix[n][i])
                }
                n--
            } else if (d == 3) {
                for (i in n downTo x) {
                    result.add(matrix[i][y])
                }
                y++
            }
            d = (d + 1) % 4

        }
        return result
    }
}