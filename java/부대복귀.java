import java.util.*;

class Solution {
    private static List<List<Integer>> graph = new ArrayList<>();
    private static int[] distance;
    
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];
        
        // 그래프 생성
        getGraph(n, roads);
        
        // 다익스트라
        distance = new int[n+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        dijkstra(destination);
        
        for(int i=0; i<sources.length; i++){
            answer[i] = distance[sources[i]] < Integer.MAX_VALUE ? distance[sources[i]] : -1;
        }
        
        return answer;
    }
    
    private void getGraph(int n, int[][] roads) {        
        for(int i=0; i<n+1; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] road: roads) {
            graph.get(road[0]).add(road[1]);
            graph.get(road[1]).add(road[0]);
        }
        
    }
    
    private void dijkstra(int destination){
        distance[destination] = 0; // 출발
        Queue<Integer> q = new LinkedList<>();
        q.add(destination);
        
        while(!q.isEmpty()){
            int current = q.poll(); // 현재 위치
            int currentDistance = distance[current]; // 현재 최단 시간
            
            for(int nxt: graph.get(current)){
                if(distance[nxt] > currentDistance + 1) {
                    distance[nxt] = currentDistance + 1;
                    q.add(nxt);
                }
            }
        }
    }
}
