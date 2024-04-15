class Solution {
    public int solution(String s) {
        int answer = 0;
        int cntX = 0;
        int cntNotX = 0;
        char x = s.charAt(0);
        
        for(int i = 0; i < s.length(); i++){
           if(cntX == cntNotX) {
               answer++;
               x = s.charAt(i);
           }
            if(s.charAt(i)==x) {
                cntX++;
            } else {
                cntNotX++;
            }
        }
        return answer;
    }
}
