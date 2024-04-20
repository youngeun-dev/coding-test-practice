import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        String[] canSpeak = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        
        for(String b: babbling){
            for(String speak: canSpeak){
                b = b.replace(speak + speak, "X").replace(speak, " ");
            }
            if(b.replace(" ","").length() == 0) answer++;
        }
        return answer;
    }
}
