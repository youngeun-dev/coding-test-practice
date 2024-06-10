import java.util.*;

class Solution {
    // 종이 조각으로 만들 수 있는 순열을 담을 Set
    private static Set<Integer> result;
    
    public int solution(String numbers) {
        int answer = 0;
        result = new HashSet<>();
       
        // 1. 모든 순열 생성
        permutation("", numbers);
        
        // 2. 소수 여부 체크
        for(Integer number: result){
            if(isPrime(number)) answer++;
        }
        
        return answer;
    }
    
    // 소수인지 판별하는 함수 
    private boolean isPrime(int number){
        if(number <= 1) return false;
        for(int i = 2; i*i <= number; i++){
            if(number % i == 0) return false;
        }
        return true;
    }
    
    // 순열을 구하는 함수
    private void permutation(String prefix, String others){
        if(!prefix.equals("")) result.add(Integer.parseInt(prefix));
        
        int n = others.length();
        for(int i=0; i<n; i++){
            permutation(prefix + others.charAt(i), others.substring(0, i) + others.substring(i + 1, n));
        }
    }
}
