import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String input = br.readLine();
        
        int m = Integer.parseInt(br.readLine());
        
        Stack<Character> left = new Stack<>();
        Stack<Character> right = new Stack<>();
        
        for(int i=0; i<input.length(); i++) {
        	left.push(input.charAt(i));
        }
        
        
        for(int i=0; i<m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	switch(st.nextToken()) {
	        	case "L":
	        		if(!left.empty()) right.push(left.pop());
	        		break;
	        	case "D":
	        		if(!right.empty()) left.push(right.pop());
	        		break;
	        	case "B":
	        		if(!left.empty()) left.pop();
	        		break;
	        	case "P":
	        		left.push(st.nextToken().charAt(0));
	        		break;
        	}
        }
        
        while(!left.empty()) {
        	right.push(left.pop());
        }
        while(!right.empty()) {
        	sb.append(right.pop());
        }
        System.out.println(sb);
    }
}
