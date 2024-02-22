# Solution 풀이
class Solution {
    fun countPrimes(n: Int): Int {
        if (n <= 2) return 0

        val nums = IntArray(n){ 1 }

        for (i in 2..Math.sqrt(n.toDouble()).toInt()){
            var j = i * i
            while (j < n){
                nums[j] = 0
                j += i
            }
        }

        return nums.sum() - 2
    }
}
