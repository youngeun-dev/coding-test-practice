import java.util.*;

// 시소 짝꿍: (몸무게 * 시소 축과 좌석 간의 거리)이 동일한 경우
class Solution {
    private static Map<Double, Integer> map = new HashMap<>();
    private static double[] distance = {1.0, 1.0/2.0, 2.0/3.0, 3.0/4,0};
    
    public long solution(int[] weights) {
        long answer = 0;
        Arrays.sort(weights);
        
        for(int weight : weights){
            for(double d : distance){
                if(map.containsKey(weight * d)){
                    answer += map.get(weight * d);
                }
            }
            map.put((double) weight, map.getOrDefault((double) weight, 0) + 1);
        }
        
        return answer;
    }
}
