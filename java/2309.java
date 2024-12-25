import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int[] heights = new int[9]; // 난쟁이 키 배열
        int fakeHeightSum = -100; // 가짜 난쟁이 키의 합

        for(int i = 0; i < 9; i++) {
            heights[i] = Integer.parseInt(reader.readLine());
            fakeHeightSum += heights[i];
        }

        int firstFake = -1, secondFake = -1;
        outerloop:
        for(int i = 0; i < 8; i++) {
            for(int j = i + 1; j < 9; j++) {
                if (heights[i] + heights[j] == fakeHeightSum) {
                    firstFake = heights[i];
                    secondFake = heights[j];
                    break outerloop;
                }
            }
        }

        Arrays.sort(heights);
        for(int height : heights){
            if(height != firstFake && height != secondFake){
                System.out.println(height);
            }
        }

    }
}
