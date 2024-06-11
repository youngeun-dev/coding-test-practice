class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int totalArea = brown + yellow;
        
        for(int width=totalArea; width>0; width--){
            if(totalArea % width > 0) continue;
               
            int height = totalArea / width;
            int y = (height - 2) * (width - 2);
            int b = totalArea - y;
            
            if (yellow == y && brown == b){
                answer[0] = width;
                answer[1] = height;
                break;
            }
            
        }
        return answer;
    }
}
