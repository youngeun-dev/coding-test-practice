import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=null;
        
        int n = Integer.parseInt(br.readLine());
        
        // a 정렬하기
        // b 의 max값과 a의 맨 앞값이랑 곱하기
        
        Integer [] a = new Integer[n];
        
        st = new StringTokenizer(br.readLine()," ");
        for(int i =0; i<n; i++) {
        	a[i]=Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(a);
        Integer [] b = new Integer[n];
        st = new StringTokenizer(br.readLine()," ");
        for(int i =0; i<n; i++) {
        	b[i]=Integer.parseInt(st.nextToken());
        }
        
        
        Integer [] temp = new Integer[n];
        for(int i =0; i<n; i++) {
        	temp[i]=b[i];
        }
        
        Arrays.sort(temp, Collections.reverseOrder());
        
        int result =0;
        for(int i =0; i<n; i++) {
        	result += temp[i]*a[i];
        }
        
        System.out.println(result);
       
    }
}
