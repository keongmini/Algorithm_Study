class Solution {
    fun reverse(x: Int): Int {
        var longX = x.toLong()              // 숫자 범위 때문에 Long type 사용
        var result = 0L

        while(longX != 0.toLong()){
            result = result * 10 + longX % 10
            longX = longX / 10
        }

        return if (Int.MAX_VALUE < result || Int.MIN_VALUE > result) 0 else result.toInt()
    }
}

// Solution
fun reverseUsingString(x: Int): Int {
    return try {
        abs(x).toString().reversed().toInt() * x.sign
    } catch (_: NumberFormatException) {
        0
    }
}

