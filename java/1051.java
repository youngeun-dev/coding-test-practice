import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(reader.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int maxLength = Math.min(N, M);

        char[][] board = new char[N][M];
        for(int i = 0; i < N; i++) {
            String input = reader.readLine();
            for(int j = 0; j < M; j++){
                board[i][j] = input.charAt(j);
            }
        }

        // 왼쪽 상단 꼭짓점 순회
        outerloop:
        while(0 < maxLength) {
            for(int i = 0; i <= N - maxLength; i++) {
                for(int j = 0; j <= M - maxLength; j++) {
                    char key = board[i][j];

                    if(board[i + maxLength - 1][j] != key) continue;
                    if(board[i][j + maxLength - 1] != key) continue;
                    if(board[i + maxLength - 1][j + maxLength - 1] != key) continue;

                    System.out.println(maxLength * maxLength);
                    break outerloop;
                }
            }
            maxLength--;
        }
    }

}
