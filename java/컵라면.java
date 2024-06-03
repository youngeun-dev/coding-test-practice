import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if(a[0] == b[0]) {
                return b[1] - a[1];
            } else {
                return a[0] - b[0];
            }
        });

        int n = Integer.parseInt(br.readLine());
        while(n-->0){
            int[] arr = new int[2];
            st = new StringTokenizer(br.readLine(), " ");
            arr[0] = Integer.parseInt(st.nextToken());
            arr[1] = Integer.parseInt(st.nextToken());
            pq.offer(arr);
        }

        PriorityQueue<Integer> select = new PriorityQueue<>();

        while(!pq.isEmpty()){
            int[] data = pq.poll();
            int deadline = data[0];
            int numOfRamen = data[1];
            if(select.size() < deadline){
                select.offer(numOfRamen);
            }else{
                if(select.peek() < numOfRamen){
                    select.poll();
                    select.offer(numOfRamen);
                }
            }
        }

        long result = 0L;
        for(Integer x: select){
            result += x;
        }
        System.out.print(result);

    }
}
