//import java.lang.*;
import java.util.*;
class Str{
	class abs{}
	public static void main(String[] args)
	{
		int x = 943566;
		String A="";
		        while(x > 0)
					        {
								            int k = x % 26;
											System.out.println(k);
											            if(k == 0)
															                A = A + 'Z';
																			            else
																							            {
																											                char c = (char) (k + 64);
																															                A = A + c;
																																			            }
																																						            x /= 26;
																																									            if(k == 0 && x == 1)
																																													                break;
																																																	        }
																																																			        StringBuffer y = new StringBuffer(A);
																																																					        y.reverse();
																																																							        A = y.toString();
		System.out.println(A);
	}
}
