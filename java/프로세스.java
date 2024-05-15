import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        // 내림차순 우선순위 큐
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int priority: priorities){
            q.offer(priority);
        }
        
        while(!q.isEmpty()){
            for(int i=0; i<priorities.length; i++){
                if (q.peek() == priorities[i]) {
                    q.poll();
                    answer++;

                    // 현재 작업이 location과 같으면 answer 반환
                    if (location == i) {
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}
