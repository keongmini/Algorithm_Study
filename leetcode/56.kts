import kotlin.math.*

class Solution {
    fun merge(intervals1: Array<IntArray>): Array<IntArray> {

        val intervals = intervals1.sortedWith(compareBy { it.elementAt(0)})
        var ans: Array<IntArray> = emptyArray<IntArray>()
        var last = 0
        ans += intervals[0]
        for(i in 0..(intervals.size-1))
        {
            if(ans[last][1] >= intervals[i][0]){
                ans[last][1] = max(ans[last][1], intervals[i][1])
            }
            else{
                ans += intervals[i]
                last++
            }
        }

        return ans
    }
}