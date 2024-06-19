import java.util.*;

class Solution {    
    private static int[] parent;
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        Arrays.sort(costs, (int[] c1, int[] c2) -> c1[2] - c2[2]);
        
        parent = new int[n];
        for(int i=0; i<n; i++) { parent[i] = i; }
        
        for(int[] edge: costs){
            int from = edge[0];
            int to = edge[1];
            int cost = edge[2];
            
            int fromParent = findParent(from);
            int toParent = findParent(to);
            
            if(fromParent == toParent) continue;
            
            answer += cost;
            parent[fromParent] = toParent;
            
        }
        return answer;
    }
    
    private int findParent(int x){
        if(parent[x] == x) return x;
        return parent[x] = findParent(parent[x]);
    }
    
}
