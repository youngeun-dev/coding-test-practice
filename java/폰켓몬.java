import java.util.*;

class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    int answer = 0;
    int choiceCnt; // 선택해야하는 폰켓몬 마리 수
    int monsterCnt; // 중복 제거한 폰켓몬 마리 수
    
    public int solution(int[] nums) {
        choiceCnt = (int) nums.length / 2;
        
        for(Integer key : nums) {
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        
        monsterCnt = map.keySet().size();
        
        return (monsterCnt < choiceCnt) ? monsterCnt : choiceCnt;
    }
}
