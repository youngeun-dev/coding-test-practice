import java.util.*;

class Solution {
    private static List<Integer> sliceArr;
    
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx = 0;
        
        for(int[] command: commands){
            sliceArr = new ArrayList<>();
            for(int i=command[0]-1; i<command[1]; i++){
                sliceArr.add(array[i]);
            }
            
            Collections.sort(sliceArr);
            
            answer[idx++] = sliceArr.get(command[2] - 1);
        }

        return answer;
    }
}
