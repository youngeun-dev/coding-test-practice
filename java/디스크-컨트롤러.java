import java.util.*;

class Solution {
    
    public int solution(int[][] jobs) {
        int answer = 0;
        int lastWork = 0;
        
        // 요청시점, 소요시간
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> (o1[1] - o2[1]));

        for(int i=0; i<jobs.length; i++){
            pq.offer(jobs[i]);
        }
        
        while(!pq.isEmpty()){
            int[] times = pq.poll();
            answer += Math.abs(lastWork - times[0]) + times[1];
            lastWork += times[1];
        }        
        
        return answer / jobs.length;
    }
}
