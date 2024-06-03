import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        while(n-->0){
            int k = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine(), " ");
            PriorityQueue<Long> pq = new PriorityQueue<>();

            for(int i=0; i<k; i++){
                pq.offer(Long.parseLong(st.nextToken()));
            }

            long answer = 0;

            while(pq.size()>1){
                Long sum = pq.poll() + pq.poll();
                pq.add(sum);
                answer += sum;
            }
            System.out.println(answer);
        }
    }
}
