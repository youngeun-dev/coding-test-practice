import java.util.*;

class Solution {
    // <전화번호, 인덱스>
    private static Map<String, Integer> phone_head = new HashMap<>();

    public boolean solution(String[] phone_book) {
        
    // 정렬
    Arrays.sort(phone_book);
        
    // map 생성
    for(int i=0; i<phone_book.length; i++){
        phone_head.put(phone_book[i], i);
    }
        
    // 접두어 존재 여부 탐색
    for(int i=0; i<phone_book.length; i++){
        for(int j=0; j<phone_book[i].length(); j++){
            if(phone_head.containsKey(phone_book[i].substring(0, j))) return false;
        }
    }
        return true;
    }
}
