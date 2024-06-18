class Solution {
    private static int maxValue;
    private static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        maxValue = -1;
        visited = new boolean[dungeons.length];
        dfs(k, 0, dungeons);
        
        return maxValue;
    }
    
    private void dfs(int k, int count, int[][] dungeons){
        for(int i=0; i<dungeons.length; i++){
            if(dungeons[i][0] <= k && !visited[i]){
                visited[i] = true;
                dfs(k - dungeons[i][1], count + 1, dungeons);
                visited[i] = false;
            }
        }
        if(maxValue < count) maxValue = count;
    }
}
