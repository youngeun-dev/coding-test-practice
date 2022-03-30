import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); // 사람의 수
        int[] time = new int[N]; // 사람 별로 인출 시간을 담을 배열

        StringTokenizer st = new StringTokenizer(br.readLine()," ");

        for(int i=0; i<N; i++){
            time[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(time);

        int sum = 0; // 총 대기시간 합계
        int prev = 0; //이전 대기 시간 + 현재 대기시간
        for(int i=0; i<N; i++){
            prev += time[i];
            sum += prev;
        }
        System.out.println(sum);
    }
}
