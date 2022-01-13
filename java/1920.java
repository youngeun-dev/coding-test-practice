import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
 
public class Main {
	
	public static int search(int[] A, int key, int start, int end) {
		while(start <= end) {
			int mid = (start+end)/2;
			
			if(A[mid]==key) {
				return 1;
			}
			else if(A[mid]<key) {
				start = mid + 1;
			}
			else {
				end = mid - 1;
			}
		}
		return -1;
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    	int n = Integer.parseInt(br.readLine());
    	int arr[] = new int[n];
    	
    	StringTokenizer st = null;
    	st = new StringTokenizer(br.readLine()," ");
    	
    	for(int i =0;i<n;i++) {
    		arr[i]=Integer.parseInt(st.nextToken());
    	}
    	
    	int m = Integer.parseInt(br.readLine());
    	int[] key = new int[m];
    	
    	st = new StringTokenizer(br.readLine()," ");
    
    	for(int i =0;i<;i++) {
    		key[i]=Integer.parseInt(st.nextToken());
    	}
    	
    	Arrays.sort(arr);
    	
    	for(int i=0; i<m;i++) {
    		if(search(arr,key[i],0,arr.length-1)==1) {
    			System.out.println(1);
    		}else {
    			System.out.println(0);
    		}
    	}
    	
       
    }
}
