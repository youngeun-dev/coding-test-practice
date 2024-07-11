import java.util.*;

class Solution {
    static int[] parent;

    public int solution(int n, int[][] computers) {
        // 부모 노드 
        parent = new int[n];
        for(int i=0; i<parent.length; i++) { parent[i] = i; }
        
        for(int i=0; i<computers.length; i++){
            for(int j=0; j<computers[0].length; j++){
                if(i==j) continue;
                if(computers[i][j] == 1){ union(i, j); }
            }
        }
        
        for(int i=0; i<parent.length; i++){
            parent[i] = find(i);
        }
        
        // 네트워크 개수 계산
        Set<Integer> set = new HashSet();
        for(int i=0; i<parent.length; i++){
            set.add(parent[i]); 
        }
        
        return set.size();

    }
    
    // 부모 업데이트 
    private void union(int node1, int node2){
        int parent1 = find(node1);
        int parent2 = find(node2);
        
        if(parent1 <= parent2) parent[parent2] = parent1;
        else parent[parent1] = parent2;
    }
    
    // 부모 노드 찾기 
    private int find(int node){
        if(parent[node] == node) return node;
        return parent[node] = find(parent[node]);
    }
    
}
