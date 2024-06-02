import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int totalWorkTime = 0; // 총 작업 시간
        int idx = 0; // 인덱스
        int completeJobs = 0; // 수행 완료된 jobs 개수
        int endTime = 0; // 종료 시간
        
        // 시작 시간 오름차순 정렬
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        // 소요 시간 오름차순 정렬
        PriorityQueue<int []> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        
        while(completeJobs < jobs.length){
            // endTime 전에 들어온 요청 pq에 추가
            while(idx < jobs.length && jobs[idx][0] <= endTime){
                pq.offer(jobs[idx++]);
            }
            
            if(!pq.isEmpty()){
                completeJobs++;
                int[] job = pq.poll();
                endTime += job[1];
                totalWorkTime += endTime - job[0];
            }else{ // pq가 비어있다면 다음 시작 시간으로 endTime 업데이트
                endTime = jobs[idx][0];
            }
            
        }
        return totalWorkTime / jobs.length;
    }
}
