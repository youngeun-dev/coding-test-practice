import java.util.*;

class Solution {
    public static int answer;
    public static List<List<Integer>> graph = new ArrayList<>();
    public static boolean[] visited;
    
    public void init(int n, int[][] edge) {
        // 가장 멀리 떨어진 노드의 개수 
        answer = 0;
        
        // 노드 그래프 
        for(int i=0; i<=n; i++) graph.add(new ArrayList<>());
        for(int[] node : edge){
            graph.get(node[0]).add(node[1]);
            graph.get(node[1]).add(node[0]);
        }
        
        // 노드 방문 여부 
        visited = new boolean[n + 1];
    }
    
    public void bfs(int n) {
        int maxValue = 0; // 가장 먼 노드의 개수
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[] {1, 0});
        visited[1] = true;
        
        while(!q.isEmpty()){
            int[] arr = q.poll();
            int node = arr[0]; // 현재 node
            int depth = arr[1]; // 현재 depth
            
            if(maxValue < depth) {
                maxValue = depth;
                answer = 1;
            } else if(maxValue == depth) { 
                answer++; 
            }
            
            for (int i = 0; i < graph.get(node).size(); i++) {
				int nextNode = graph.get(node).get(i); // 다음 node
                if(!visited[nextNode]){
                    visited[nextNode] = true;
                    q.add(new int[] {nextNode, depth + 1});
                }
            }
        }
    }
    
    public int solution(int n, int[][] edge) {
        init(n, edge);
        bfs(n);
        
        return answer;
    }
}
