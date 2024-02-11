class Solution {
    fun setZeroes(matrix: Array<IntArray>): Unit {
        val n = matrix.indices        // like 0..2 (IntRange)
        val m = matrix[0].indices

        val rows = IntArray(matrix.size)        // int[matrix.size]
        val cols = IntArray(matrix[0].size)

        for (i in n) for (j in m)           // 0을 가지고 있는 인덱스에 표시해주기
            if (matrix[i][j] == 0) {
                rows[i]++
                cols[j]++
            }

        for (i in n) if (rows[i] > 0) for (j in m) matrix[i][j] = 0
        for (j in m) if (cols[j] > 0) for (i in n) matrix[i][j] = 0
    }
}

// in-place 알고리즘에 대해 더 알아보기
