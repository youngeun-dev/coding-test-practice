import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	public static int lowerBound(List<Integer> list, int key) {
		int start = 0;
		int end = list.size();
		
		while (start < end) {
			int mid = (start + end) / 2;
			if (list.get(mid) >= key) {
				end = mid;
			} else {
				start = mid + 1;
			}
		}
		return start;
	}

	public static int upperBound(List<Integer> list, int key) {
		int start = 0;
		int end = list.size();
		
		while (start < end) {
			int mid = (start + end) / 2;
			
			if (list.get(mid) <= key) {
				start = mid + 1;
			} else {
				end = mid;
			}
		}
		return start;
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int n = Integer.parseInt(br.readLine());
		List<Integer> list1 = new ArrayList<Integer>(n);

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < n; i++) {
			list1.add(Integer.parseInt(st.nextToken()));
		}

		list1.sort(null);

		int m = Integer.parseInt(br.readLine());
		List<Integer> list2 = new ArrayList<Integer>(m);

		StringBuilder sb = new StringBuilder();

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < m; i++) {
			list2.add(Integer.parseInt(st.nextToken()));

			sb.append(upperBound(list1, list2.get(i)) - lowerBound(list1, list2.get(i))).append(' ');

		}

		System.out.print(sb);
		
	}
}



