class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {
        val ans = MutableList(0){MutableList<Int>(0){0}}
        if (n==0 || k==0){
            return ans
        }
        dfs(ans, 1, n, k, MutableList<Int>(0){0})
        return ans
    }
    fun dfs(ans: MutableList<MutableList<Int>>, index: Int, n: Int, k: Int, tmp: MutableList<Int>): Unit{
        if (tmp.size == k){
            val t = MutableList(k){i->tmp[i]}
            ans.add(t)
            return
        }
        for (i in index .. n){
            tmp.add(i)
            dfs(ans, i+1, n, k, tmp)
            tmp.removeAt(tmp.size-1)
        }
    }
}