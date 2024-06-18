import java.util.*;

class Solution {
    private static List<String> dictionary;
    private static char[] aeiou = {'A', 'E', 'I', 'O', 'U'};
    
    public int solution(String word) {
        dictionary = new ArrayList<>();
        dfs("");
        
        int answer = 0;
        for(int i=0; i<dictionary.size(); i++){
            if(dictionary.get(i).equals(word)){
                answer = i;
                break;
            }
        }
        return answer + 1;
    }
    
    private void dfs(String word){
        if(word != "") dictionary.add(word);
        if(word.length() == 5) return;
        
        for(int i=0; i<5; i++){
            dfs(word + aeiou[i]);
        }
    }
}
