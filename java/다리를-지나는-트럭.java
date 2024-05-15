import java.util.*;

class Solution {
    private static Queue<Integer> trucks;
    private static Queue<Integer> bridge;

    private static void init(int bridge_length, int[] truck_weights){
        trucks = new LinkedList<>();
        bridge = new LinkedList<>();
        
        // 트럭 무게 초기화
        for(int truck_weight: truck_weights){
            trucks.offer(truck_weight);
        }
        // 초기 다리 값 초기화
        for(int i=0; i<bridge_length; i++){
            bridge.offer(0);
        }
    }
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = bridge_length;
        int bridge_weights = 0;
        
        // bridge, trucks 큐 생성
        init(bridge_length, truck_weights);
        
        // 남은 트럭이 있을 때까지
        while(!trucks.isEmpty()){
            time ++;
            
            // 다리에서 트럭을 내린다
            bridge_weights -= bridge.poll();
            
            // 다음 트럭 무게
            int next_truck_weight = trucks.peek();

            // 무게를 초과한 경우 
            if (bridge_weights + next_truck_weight > weight){
                bridge.offer(0);
            }
            // 다음 트럭이 다리에 오를 수 있는 경우
            else {
                bridge_weights += next_truck_weight;
                bridge.offer(next_truck_weight);
                trucks.poll();
            }

        }
        
        return time;
    }
}
