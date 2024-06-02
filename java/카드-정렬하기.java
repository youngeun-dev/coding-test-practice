import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int n = Integer.parseInt(br.readLine()); 
        while(n-->0) pq.add(Integer.parseInt(br.readLine())); 

        int answer = 0;
        while(pq.size() > 1){
            int sum = pq.poll() + pq.poll();
            answer+=sum;
            pq.add(sum);
        }
        System.out.print(answer);
    }
}
