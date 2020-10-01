import java.util.*;
import java.io.*;

public class Solution{

	public static void main(String[] args){
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		//The first T entered indicates how many use cases follow.
		int T = in.nextInt();
		//Cyclic processing of each use case
		for(int i = 1; i <= T; i++){
			//Get a number N
			long N = in.nextLong();
			//Converting long-type values to strings
			String s = String.valueOf(N);
			//Converting strings to int arrays
			//Both find functions modify array elements directly, so you need to pass two
			//Setting s.length()+1 is to give a possible increase in the number of bits left.
			int[] array = new int[s.length() + 1];
			int[] array1 = new int[s.length() + 1];
			//The trick is to traverse from j = 1 and leave a place for array[0]. There may be situations where you need to add 2 at the front.
			for(int j = 1; j <= s.length(); j++){
				array[j] = Integer.parseInt(s.substring(j-1, j));
				array1[j] = array[j];
			}
			//Find the largest "beautiful" integer smaller than N
			long X = findX(array);
			//Find the smallest "beautiful" integer larger than N
			long Y = findY(array1);
			long ans = Math.min(Math.abs(N - X), Math.abs(Y - N));
			System.out.printf("Case #%d: %d\n", i, ans);
		}
		in.close();
	}
	
	public static long findX(int[] array){
		boolean firstOdd = false;
		//Cyclic traversal, find the first odd number minus 1, and then change the number to 8.
		for(int i = 1; i < array.length; i++){
			//If the number is odd, there are two cases: 1. It is the first odd number, minus one; 2. It is not the first odd number, that is, the number after the first odd number, instead of 8.
			if(array[i] % 2 != 0){
				//And it's the first odd number.
				if(!firstOdd){
					array[i]--;
					firstOdd = true;
				}else{
					//Not the first odd number
					array[i] = 8;
				}
			//If the number is not an odd number, there are two cases: 1. the number before the first odd number is not treated; 2. the number after the first odd number is changed to 8.
			}else{
				if(firstOdd){
					array[i] = 8;
				}
			}
		}
		//Converting an int array to a long-type value
		long X = 0;
		for(int i = 0; i < array.length; i++){
			X = X * 10 + array[i];
		}
		return X;
	}
	
	public static long findY(int[] array){
		boolean firstOdd = false;
		
		//Cyclic traversal, find the first odd number plus 1, the latter number is changed to 0
		for(int i = 1; i < array.length; i++){
			if(array[i] % 2 != 0){
				//If it's the first odd number
				if(!firstOdd){
					//First judge whether it is 9, if it is 9, then change to 0. Circular judge whether it is 8, 8 to 0, not 8 plus 2?
					if(array[i] == 9){
						array[i] = 0;
						int j = i - 1;
						while(array[j] == 8){
							array[j] = 0;
							j--;
						}
						array[j] += 2;
					}else{
						//Not 9 plus 1 directly
						array[i] ++;
					}
					firstOdd = true;
				}else{
					//If it is not the first odd number, then the odd number after the first odd number is changed to 0.
					array[i] = 0;
				}
			}else{
				if(firstOdd){
					array[i] = 0;
				}
			}
		}
		long Y = 0;
		for(int i = 0; i < array.length; i++){
			Y = Y * 10 + array[i];
		}
		return Y;
	}
}
