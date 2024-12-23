import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int target = Integer.parseInt(reader.readLine());
        int answer = 0;

        for(int i = 0; i <= 1000000; i++){
            int sum = i;
            int currentNum = i; // 각 자리수 계산용

            while(currentNum != 0){
                sum += currentNum % 10;
                currentNum /= 10;
            }

            if(sum == target) {
                answer = i;
                break;
            }
        }
        System.out.println(answer);
    }
}
