import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
 
public class Main {

    public static void main(String[] args) throws Exception {
    	
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = null;
    	
    	int n = Integer.parseInt(bf.readLine());
    	
    	Stack<Integer> stack = new Stack<>();
    	
    	for(int i =0; i<n; i++) {
    		st = new StringTokenizer(bf.readLine()," ");
    		switch(st.nextToken()) {
    		case "push":
    			stack.push(Integer.parseInt(st.nextToken()));
    			break;
    		case "top":
    			if(stack.empty()) {
    				System.out.println(-1);
    			}else{
    			System.out.println(stack.peek());
    			}
    			break;
    		case "pop":
    			if(stack.empty()) {
    				System.out.println(-1);
    			}else{
    				System.out.println(stack.pop());
    			}
    			break;
    		case "size":
    			System.out.println(stack.size());
    			break;
    		case "empty":
    			if(stack.empty()) {
    				System.out.println(1);
    			}else {
    				System.out.println(0);
    			}
    			break;
    		}
    	}
    	

    }	
}
