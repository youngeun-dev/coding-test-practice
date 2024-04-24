import java.util.*;

// -------------------------------------------------------------

class Solution {
    public String solution(String new_id) {
        String answer = "";
        
        // 1
        new_id = new_id.toLowerCase();
        
        // 2
        for(int i=0; i<new_id.length(); i++){
            char c = new_id.charAt(i);
            if(Character.isAlphabetic(c) || 
               Character.isDigit(c) || 
               c == '.' || c == '-' || c == '_') {
                answer += c;
            }
        }
        
        // 3
        while(answer.indexOf("..") != -1) {
            answer = answer.replace("..", ".");
        }
        
        // 4
        if(!answer.isEmpty() && answer.charAt(0) == '.') {
            answer = answer.substring(1);
        }
        
        if(!answer.isEmpty() && answer.charAt(answer.length() - 1) == '.') {
            answer = answer.substring(0, answer.length() - 1);
        }
        
        // 5
        if(answer.isEmpty()) { answer += 'a'; }

        // 6
        if(answer.length() >= 16) { 
            answer = answer.substring(0, 15); 
            if(answer.charAt(answer.length() - 1) == '.') {
                answer = answer.substring(0, answer.length() - 1);
            }
        }
        
        // 7 
        while(answer.length() < 3) {
            answer += answer.charAt(answer.length() - 1);
        }

        return answer;
    }
}

// -------------------------------------------------------------

class Solution {
    public String solution(String new_id) {
        return new KakaoId(new_id)
            .noUpperCase()
            .filter()
            .noDoubleDot()
            .noSideDot()
            .noEmpty()
            .checkMaxLength()
            .checkMinLength()
            .getId();
    }
    
    private static class KakaoId {
        private String id;
        
        KakaoId(String id) { this.id = id; }
        
        private KakaoId noUpperCase() { 
            id = id.toLowerCase();
            return this;
        }
        
        private KakaoId filter() {
            id = id.replaceAll("[^-_.a-z0-9]", "");
            return this;
        }
        
        private KakaoId noDoubleDot() {
            while(id.contains("..")) {
                id = id.replace("..", ".");
            }
            return this;
        }
        
        private KakaoId noSideDot() {
            // 맨앞 . 제거
            if(!id.isEmpty() && id.charAt(0) == '.') { id = id.substring(1); }
            // 맨뒤 . 제거
            if(!id.isEmpty() && id.charAt(id.length() - 1) == '.') { id = id.substring(0, id.length() - 1); }
            return this;
        }
        
        private KakaoId noEmpty() {
            if(id.isEmpty()) { id = "a"; }
            return this;
        }
        
        private KakaoId checkMaxLength() {
            if(id.length() >= 16) { 
                id = id.substring(0, 15);
                if(id.charAt(id.length() - 1) == '.') { 
                    id = id.substring(0, id.length() - 1); 
                }
            }
            return this;
        }
        
        private KakaoId checkMinLength() {
            while(id.length() < 3){
                id += id.charAt(id.length() - 1);
            }
            return this;
        }
        
        private String getId() {
            return id;
        }
    }
}
