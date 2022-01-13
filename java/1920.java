import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
 
public class Main {
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
        int N = Integer.parseInt(br.readLine());
        
        ArrayList<Integer> arr = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }
        
        Collections.sort(arr);
        
        StringBuilder sb = new StringBuilder();
        for(int val:arr) {
        	sb.append(val).append('\n');
        }
        System.out.println(sb);
}
}



// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.Arrays;
// import java.util.StringTokenizer;
 
// public class Main {
	
// 	public static int search(int[] A, int key, int start, int end) {
// 		while(start <= end) {
// 			int mid = (start+end)/2;
			
// 			if(A[mid]==key) {
// 				return 1;
// 			}
// 			else if(A[mid]<key) {
// 				start = mid + 1;
// 			}
// 			else {
// 				end = mid - 1;
// 			}
// 		}
// 		return -1;
// 	}
	
//     public static void main(String[] args) throws IOException {
//     	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
//     	int n = Integer.parseInt(br.readLine());
//     	int arr[] = new int[n];
    	
//     	StringTokenizer st = null;
//     	st = new StringTokenizer(br.readLine()," ");
    	
//     	for(int i =0;i<n;i++) {
//     		arr[i]=Integer.parseInt(st.nextToken());
//     	}
    	
//     	int m = Integer.parseInt(br.readLine());
//     	int[] key = new int[m];
    	
//     	st = new StringTokenizer(br.readLine()," ");
    
//     	for(int i =0;i<;i++) {
//     		key[i]=Integer.parseInt(st.nextToken());
//     	}
    	
//     	Arrays.sort(arr);
    	
//     	for(int i=0; i<m;i++) {
//     		if(search(arr,key[i],0,arr.length-1)==1) {
//     			System.out.println(1);
//     		}else {
//     			System.out.println(0);
//     		}
//     	}
    	
       
//     }
// }






// import java.io.BufferedReader;
// import java.io.InputStreamReader;
// import java.util.Arrays;
 
// public class Main {
 
//     public static void main(String[] args) throws Exception {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 
//         int N = Integer.parseInt(br.readLine());
//         Integer[] arr = new Integer[N];
 
//         for (int i = 0; i < N; i++) {
//             arr[i] = Integer.parseInt(br.readLine());
//         }
        
//         // 타입이 primitive가 아닌, Object이다.
//         Arrays.sort(arr);
 
//         for(int val:arr) {
//         	System.out.println(val);
//         }
// }
// }
