class Solution {
    fun maxArea(height: IntArray): Int {

        var left = 0
        var right = height.size - 1

        var result = 0

        while (left < right){
            var now = (right - left) * min(height[left], height[right])

            result = max(result, now)

            if(height[left] < height[right]){
                left ++
            }else{
                right --
            }
        }

        return result
    }
}