import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");
        int selectedCard1 = Integer.parseInt(st.nextToken());
        int selectedCard2 = Integer.parseInt(st.nextToken());

        double totalCases = 153.0;
        int winningCases;

        // 영학 == 땡
        if (selectedCard1 == selectedCard2) {
            winningCases = 153 - (10 - selectedCard1); // 영학이가 이길 경우의 수
            System.out.print(formatNum(winningCases / totalCases));
        }

        // 영학 == 끗
        else {
            int target = (selectedCard1 + selectedCard2) % 10; // 영학이의 일의 자리 수
            winningCases = 0; // 영학이가 이길 경우의 수

            // 상대의 패 탐색 (상대가 땡 나오면 영학이가 짐 -> 땡 안나오도록)
            for (int i = 1; i <= 10; i++) {
                for (int j = i + 1; j <= 10; j++) {
                    // 영학이가 이길 경우의 수 (상대의 일의 자리수가 작은 경우)
                    if ((i + j) % 10 < target) {
                        if (i == selectedCard1 || i == selectedCard2 || j == selectedCard1 || j == selectedCard2) { // 영학이가 뽑은 카드는 뽑을 수 없음
                            winningCases += 2;
                        } else {
                            winningCases += 4;
                        }
                    }
                }
            }
            System.out.println(formatNum(winningCases / totalCases));
        }

    }

    private static String formatNum(double num) {
        return String.format("%.3f", num);
    }
}
