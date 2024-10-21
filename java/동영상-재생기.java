import java.util.*;

class Solution {
    public static Map<String, Integer> map = new HashMap<>();
    public static Integer openingStart;
    public static Integer openingEnd;
    public static Integer totalVideoLen;
    
    public static void init() {
        map.put("next", 10);
        map.put("prev", -10);
    }
    
    public Integer toSecond(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
    
    public String toString(Integer time) {
        return String.format("%02d:%02d", time / 60, time % 60);
    }
    
    public Boolean isOpening(Integer time) {
        return openingStart <= time && time <= openingEnd;
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        init();
        openingStart = toSecond(op_start);
        openingEnd = toSecond(op_end);
        totalVideoLen = toSecond(video_len);
        
        Integer current = toSecond(pos);
        for (String command : commands) {
            // 오프닝 건너뛰기
            if (isOpening(current) == true) {
                current = openingEnd;
            }
            
            // 명령에 맞는 위치 이동
            current += map.get(command);
            
            // 영상 구간을 벗어난 경우 
            if (current < 0) current = 0;
            else if (totalVideoLen < current) current = totalVideoLen;
        }
        
        // 마지막 위치가 오프닝 구간인 경우
        if (isOpening(current) == true) { 
            current = openingEnd;
        }

        return toString(current);
    }
}
