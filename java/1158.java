import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		StringBuilder sb = new StringBuilder();
		sb.append('<');
		
		Queue<Integer> queue = new LinkedList<>();

		for (int i = 1; i <= n; i++) {
			queue.add(i);
		}

		while (queue.size()>1) {
			for (int i = 1; i < k; i++) {
				queue.add(queue.poll());
			}
			sb.append(queue.poll()+", ");
		}
		
		sb.append(queue.poll()).append('>');
		System.out.println(sb); 
	}
}
