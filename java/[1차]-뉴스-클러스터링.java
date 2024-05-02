import java.util.*;

class Solution {
    private static double answer = 0;
    private static double sameCnt = 0;
    private static double unionCnt = 0;
    
    private static List<String> str1List = new ArrayList<>();
    private static List<String> str2List = new ArrayList<>();
    
    private static List<String> makeStrList(List<String> strList, String str){
        for(int i = 0; i < str.length() - 1; i++){
            if(Character.isAlphabetic(str.charAt(i)) && Character.isAlphabetic(str.charAt(i+1))){
                strList.add(str.substring(i, i+2));
            }
        }
        return strList;
    }

    public static int solution(String str1, String str2) {
        // 소문자 변환
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        
        // 집합 리스트 생성
        str1List = makeStrList(str1List, str1);
        str2List = makeStrList(str2List, str2);
                
        // 모두 공집합
        if(str1List.isEmpty() && str2List.isEmpty()) return 65536;
        
        // 교집합 
        for (String s : str1List) {
            if(str2List.remove(s)){
                sameCnt += 1;
            }
            unionCnt += 1;
        }
        
        // 합집합
        for (String s : str2List) {
            unionCnt += 1;
        }
        
        answer = sameCnt / unionCnt;

        return (int) (answer * 65536);
    }
}
