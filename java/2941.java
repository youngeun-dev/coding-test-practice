import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int count = 0;
		String str = br.readLine();

		for (int i = 0; i < str.length(); i++) {
			
			char c = str.charAt(i);

			if (c == 'c' && i < str.length() - 1) {
				if (str.charAt(i + 1) == '=' || str.charAt(i + 1) == '-') {
					i++;
				}
			}

			if (c == 'd' && i < str.length() - 1) {
				if (str.charAt(i + 1) == '-') {
					i++;
				} else if (str.charAt(i + 1) == 'z' && i < str.length() - 2) {
					if (str.charAt(i + 2) == '=') {
						i += 2;
					}
				}
			}

			if (c == 'l' && i < str.length() - 1) {
				if (str.charAt(i + 1) == 'j') {
					i++;
				}
			}

			if (c == 'n' && i < str.length() - 1) {
				if (str.charAt(i + 1) == 'j') {
					i++;
				}
			}

			if (c == 's' && i < str.length() - 1) {
				if (str.charAt(i + 1) == '=') {
					i++;
				}
			}

			if (c == 'z' && i < str.length() - 1) {
				if (str.charAt(i + 1) == '=') {
					i++;
				}
			}
			
			count++;
		}
		
		System.out.println(count);

	}
}
