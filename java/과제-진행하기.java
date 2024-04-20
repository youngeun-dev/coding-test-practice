// ---------------------------------------------------------------------------------------
import java.util.*;

class Plan{
    String subject;
    int startAt;
    int remainTime;
    
    Plan(String subject, int startAt, int remainTime){
        this.subject = subject;
        this.startAt = startAt;
        this.remainTime = remainTime;
    }
    
    public String getSubject(){
        return this.subject;
    }
    
    public int getStartAt(){
        return this.startAt;
    }
    
    public int getEndAt(){
        return this.startAt + this.remainTime;
    }
    
    public int getRemainTime(){
        return this.remainTime;
    }
    
    public void updateRemainTime(int remainTime){
        this.remainTime = remainTime;
    }
}

class Solution {
    
    // 시:분 -> 분 단위로 변경
    public int changeTimeUnit(String time){
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
    
    // Plan 객체 생성
    public Plan getPlan(String[] plan) {
        int startAt = changeTimeUnit(plan[1]);
        return new Plan(plan[0], startAt, Integer.parseInt(plan[2]));
    }
    
    public List<String> solution(String[][] plans) {
        // 끝낸 과제 
        List<String> answer = new ArrayList<>();
        
        // 남은 과제 
        List<Plan> stop = new ArrayList<>();
        
        // [과목명, 시작시간, 남은시간]
        Plan[] todoList = new Plan[plans.length];
        for(int i=0; i<plans.length; i++){
            todoList[i]  = getPlan(plans[i]);
        }
        
        // 시작 시간 기준 오름차순 정렬
        Arrays.sort(todoList, (x1, x2) -> Integer.compare(x1.getStartAt(), x2.getStartAt()));
        
        for(int i=0; i<todoList.length - 1; i++){
            String nowSubject = todoList[i].getSubject();
            int nowRemainTime = todoList[i].getRemainTime();
            int nowEndAt = todoList[i].getEndAt();
            int nxtStartAt = todoList[i+1].getStartAt();
            
            // 1. 과제 종료 시간 <= 다음 과제 시작시간
            if(nowEndAt <= nxtStartAt){
                answer.add(nowSubject);
                
                // 수행 중 멈춘 과제가 있다면
                int availableTime = nxtStartAt - nowEndAt;
                while(!stop.isEmpty() && availableTime > 0){
                    int lastIdx = stop.size() - 1;
                    int remainTime = stop.get(lastIdx).getRemainTime() - availableTime;
                    stop.get(lastIdx).updateRemainTime(remainTime);
                    availableTime = remainTime * -1;
                    if(remainTime <= 0) {
                        answer.add(stop.get(lastIdx).getSubject());
                        stop.remove(lastIdx);
                    }
                }
            }
            
            // 2. 과제 종료 시간 > 다음 과제 시작시간
            else {
                todoList[i].updateRemainTime(nowRemainTime - (nxtStartAt - todoList[i].getStartAt()));
                stop.add(todoList[i]);
            }
        }
        
        // 남은 과제 수행
        answer.add(todoList[todoList.length - 1].getSubject());
        while(!stop.isEmpty()){
            int lastIdx = stop.size() - 1;
            answer.add(stop.get(lastIdx).getSubject());
            stop.remove(lastIdx);
        }



// --------------------------------------------------------------------------------------------------
// 2. use stack
import java.util.*;
import java.util.stream.Collectors;

class Plan{
    String subject;
    int startAt;
    int remainTime;
    
    Plan(String subject, int startAt, int remainTime){
        this.subject = subject;
        this.startAt = startAt;
        this.remainTime = remainTime;
    }
    
    public String getSubject(){
        return this.subject;
    }
    
    public int getStartAt(){
        return this.startAt;
    }
    
    public int getEndAt(){
        return this.startAt + this.remainTime;
    }
    
    public int getRemainTime(){
        return this.remainTime;
    }
    
    public void updateRemainTime(int remainTime){
        this.remainTime = remainTime;
    }
}

class Solution {
    
    // 시:분 -> 분 단위로 변경
    public int changeTimeUnit(String time){
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
    
    // Plan 객체 생성
    public Plan getPlan(String[] plan) {
        return new Plan(plan[0], changeTimeUnit(plan[1]), Integer.parseInt(plan[2]));
    }
    
    public List<String> solution(String[][] plans) {
        // 끝낸 과제 
        List<String> answer = new ArrayList<>();
        
        // 남은 과제 
        Stack<Plan> stop = new Stack<>();
        
        // [과목명, 시작시간, 남은시간]
        List<Plan> todoList = new ArrayList<>();
        for (int i = 0; i < plans.length; i++) {
            todoList.add(getPlan(plans[i]));
        }

        // 시작 시간 기준 오름차순 정렬
        todoList = todoList.stream()
                            .sorted(Comparator.comparing(Plan::getStartAt))
                            .collect(Collectors.toList());
        
        
        for(int i=0; i<todoList.size() - 1; i++){
            Plan now = todoList.get(i);
            Plan nxt = todoList.get(i + 1);
            
            // 1. 과제 종료 시간 <= 다음 과제 시작시간
            if(now.getEndAt() <= nxt.getStartAt()){
                answer.add(now.getSubject());
                
                // 수행 중 멈춘 과제가 있다면
                int availableTime = nxt.getStartAt() - now.getEndAt();
                while(!stop.isEmpty() && availableTime > 0){
                    int remainTime = stop.peek().getRemainTime() - availableTime;
                    stop.peek().updateRemainTime(remainTime);
                    availableTime = remainTime * -1;
                    if(remainTime <= 0) { answer.add(stop.pop().getSubject()); }
                }
            }
            
            // 2. 과제 종료 시간 > 다음 과제 시작시간
            else {
                now.updateRemainTime(now.getRemainTime() - (nxt.getStartAt() - now.getStartAt()));
                stop.push(now);
            }
        }
        
        // 남은 과제 수행
        answer.add(todoList.get(todoList.size() - 1).getSubject());
        while(!stop.isEmpty()){
            answer.add(stop.pop().getSubject());
        }
        
        return answer;
    }
}        
        return answer;
    }
}
