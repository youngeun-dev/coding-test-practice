import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
 
public class Main {

    public static void main(String[] args) throws Exception {
    	
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = null;
    	
      int back = 0;
    	int n = Integer.parseInt(bf.readLine());
    	
    	Queue<Integer> queue = new LinkedList<>();
    	
    	for(int i =0; i<n; i++) {
    		st = new StringTokenizer(bf.readLine()," ");
    		switch(st.nextToken()) {
    		case "push":
    			back = Integer.parseInt(st.nextToken());
    			queue.offer(back);
    			break;
    		case "front":
    			if(queue.isEmpty()) {
    				System.out.println(-1);
    			}else{
    			System.out.println(queue.peek());
    			}
    			break;
    		case "back":
    			if(queue.isEmpty()) {
    				System.out.println(-1);
    			}else{
    			System.out.println(back);
    			}
    			break;
    		case "pop":
    			if(queue.isEmpty()) {
    				System.out.println(-1);
    			}else{
    				System.out.println(queue.poll());
    			}
    			break;
    		case "size":
    			System.out.println(queue.size());
    			break;
    		case "empty":
    			if(queue.isEmpty()) {
    				System.out.println(1);
    			}else {
    				System.out.println(0);
    			}
    			break;
    		}
    	}
    	

    }	
}
