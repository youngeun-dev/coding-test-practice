import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine()); // 회의의 수
        int[][] time = new int[N][2]; // 시작 시간, 종료 시간

        for(int i = 0; i < N; i++){ // 회의 시간 N번 입력
             st = new StringTokenizer(br.readLine()," ");
             time[i][0] = Integer.parseInt(st.nextToken()); // 시작 시간
             time[i][1] = Integer.parseInt(st.nextToken()); // 종료 시간
        }

        Arrays.sort(time, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[1] == o2[1]){ // 종료 시간이 같을 경우 시작 시간이 빠른순으로 정렬한다.
                    return o1[0] - o2[0];
                }
                return o1[1] - o2[1];
            }
        });

        int count = 0; // 회의 개수
        int end_time = 0;

        for(int i = 0; i < N; i++){
            if(end_time <= time[i][0]){
                count++;
                end_time = time[i][1];
            }
        }

        System.out.println(count);
    }
}
