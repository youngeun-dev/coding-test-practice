import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
    
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()); // 입력 받을 개수

		StringBuilder sb = new StringBuilder();
		Stack<Integer> stack = new Stack<>();

		int last_value = 0; // 마지막 입력 값

		for (int i = 0; i < n; i++) { // n번 반복
			int value = Integer.parseInt(br.readLine()); // 값 입력

			if (last_value < value) { // 입력한 값이 마지막으로 입력한 값보다 크면 실행
				for (int j = last_value + 1; j <= value; j++) {
					stack.push(j); // 오름차순으로 스택에 push
					sb.append('+').append('\n');
				}
				last_value = value; // 마지막 입력 값을 바꾸어 준다.
			} else {
				if (stack.peek() != value) { // stack의 top이 입력한 값과 다르면 NO
					System.out.println("NO");
					return;
				}
			}
			stack.pop();
			sb.append('-').append('\n');
		}
		System.out.println(sb);
	}
}
