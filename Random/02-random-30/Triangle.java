
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[]dp = new int[n+1];
        for(int i=n-1; i>=0;i--){
            for(int j=0;j<triangle.get(i).size();j++){
                int currElement = triangle.get(i).get(j);
                dp[j] = Math.min(dp[j],dp[j+1]) + currElement;
            }
        }
        return dp[0];
    }
}