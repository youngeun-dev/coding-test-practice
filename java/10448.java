import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int[] triNum = new int[44]; // 삼각수 배열
        for(int i = 1; i < 45; i++) {
            triNum[i - 1] = i * (i + 1) / 2;
        }

        int T = Integer.parseInt(reader.readLine());

        while(T > 0) {
            T--;
            int result = 0;
            int target = Integer.parseInt(reader.readLine());

            outerloop:
            for(int i = 0; i < 44; i++) {
                if(triNum[i] > target) { break; }
                for(int j = 0; j < 44; j++) {
                    if(triNum[i] + triNum[j] > target) { break; }
                    for(int k = 0; k < 44; k++) {
                        int sum = triNum[i] + triNum[j] + triNum[k];
                        if(sum > target) { break; }
                        if(sum == target) {
                            result = 1;
                            break outerloop;
                        }
                    }
                }
            }

            System.out.println(result);
        }
    }
}
