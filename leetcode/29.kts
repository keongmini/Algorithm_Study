class Solution {
    fun divide(dividend: Int, divisor: Int): Int {
        if(dividend== -2147483648 && divisor== -1) return 2147483647;
        return (dividend/divisor).toInt();
    }
}