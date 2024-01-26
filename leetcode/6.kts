class Solution {
    fun convert(s: String, numRows: Int): String {
        if(numRows == 1){
            return s
        }

        var result = StringBuilder()
        val n = s.length
        val interval = 2 * numRows - 2

        for (i in 0 until numRows){     // until == range(py)
            for(j in i until n step interval){
                result.append(s[j])
                if(i != 0 && i != numRows - 1 && j + interval - 2 * i < n){     // 칸씩 뛰어넘으면서 해당 인덱스에 있는 값 저장
                    result.append(s[j + interval - 2 * i])
                }
            }
        }

        return result.toString()
    }
}