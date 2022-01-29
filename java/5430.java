import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int testCase = Integer.parseInt(br.readLine()); // 테스트 케이스 횟수 입력

		while (testCase-- > 0) {
			
			String command = br.readLine(); // 명령어 입력
			int n = Integer.parseInt(br.readLine()); // 배열 원소 개수
			Deque<Integer> q = new ArrayDeque<>(); 
			
			st = new StringTokenizer(br.readLine(), "[],");
			for (int i = 0; i < n; i++) {
				q.add(Integer.parseInt(st.nextToken())); // 값 입력
			} 
			
			boolean isRight = true; // 정방향인지 역방향인지 확인하는 변수
			for (char c : command.toCharArray()) {

				if (c == 'R') { // R이면 방향을 바꾸어준다.
					isRight = !isRight;
					continue;
				}
				
				if (c == 'D') {
					if (isRight) { // D인데 정방향이면 첫번째 원소를 remove, 값이 없다면 에러 메세지 추가
						if (q.pollFirst() == null) {
							sb.append("error").append('\n');
							return;
						}
					} else { // D인데 역방향
						if (q.pollLast() == null) {
							sb.append("error").append('\n');
							return;
						}
					}
				}

				print(q,isRight);
			}
			
		}
		System.out.println(sb);
	}
	
	public static void print(Deque<Integer> q, boolean isRight) {
		sb.append('[');

		if (q.size() > 0) { // q가 존재할 때까지

			if (!isRight) { // 역방향이면 뒤에서부터 출력
				sb.append(q.pollLast()); 
				while (!q.isEmpty()) {
					sb.append(',').append(q.pollLast());
				}
			} else {
				sb.append(q.pollFirst());
				while (!q.isEmpty()) {
					sb.append(',').append(q.pollFirst());
				}
			}
		}
		sb.append(']').append('\n');
	}
}
