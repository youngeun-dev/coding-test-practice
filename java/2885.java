import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int k = Integer.parseInt(br.readLine()); // 먹을 초콜릿
        int size = 1;
        int size2 = 0;
        int count = 0;

        while (size < k) {
            size *= 2;
            size2 = size;
        }
        // size 가 k보다 작다면 계속 제곱을 시켜줘서 최소 초콜릿 크기를 구함

        while (k > 0) {
            if (k < size) {
                size /= 2;
                count++;
            }
            // size가 k보다 더 크다면 size를 2분의 1로 나눠주고 count를 증가시킴
            else {
                k -= size;
            }
            // size가 k보다 작거나 같다면 구해야하는 초콜릿 크기를 줄여나감
        }
        System.out.println(size2 + " " + count);
    }
}
