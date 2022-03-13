/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for(int i=0;i<t;i++){
		    int a = sc.nextInt();
		    int b = sc.nextInt();
		    int c = a + b;
		    int m = 0;
		    for(int j=1;j<c;j++){
		        if(j%2!=0){
		            
		            if(a-j<0){
		                a -= j;
		                m = 1;   // This means that Bob wins
		                break;
		            }
		            else{
		                a -= j;
		                continue;
		            }
		        }
		        else{
		            if(b-j<0){
		                b -= j;
		                m = 2;  // This means that Limak wins 
		                break;
		            }
		            else{
		                b -= j;
		                continue;
		            }
		        }
		    }
		    
		    if(m==1){
		        System.out.println("Limak");
		    }
		    else{
		        System.out.println("Bob");
		    }
		}
	}
}
