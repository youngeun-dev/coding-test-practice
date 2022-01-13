import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
 
public class Main {
	public static int search(int[] arr, int key, int start, int end) {
		while(start <= end) {
			int mid =(start+end)/2;
			if(arr[mid]==key) {
				return 1;
			}
			else if(arr[mid] < key) {
				start = mid + 1;
			}
			else {
				end = mid - 1;
			}
		}
		return 0;
	}
 
    public static void main(String[] args) throws Exception {
    	
    	BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = null;
    	
    	
    	int n = Integer.parseInt(bf.readLine());
    	int[] arr = new int[n];
    	st = new StringTokenizer(bf.readLine()," ");

    	
    	for(int i=0; i<n; i++) {
    		arr[i]=Integer.parseInt(st.nextToken());
    	}
    	
    	int m = Integer.parseInt(bf.readLine());
    	int[] key = new int[m];
    	
    	st = new StringTokenizer(bf.readLine()," ");

    	for(int i=0; i<m; i++) {
    		key[i]=Integer.parseInt(st.nextToken());
    	}
    	
    	Arrays.sort(arr);
    	
    	for(int i =0; i<m; i++) {
    		if(search(arr,key[i],0,arr.length -1)==1) {
    			System.out.println(1);
    		}else {
    			System.out.println(0);
    		}
    	}

    }	
}
