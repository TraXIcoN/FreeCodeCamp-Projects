import java.io.*;
import java.util.*;
import java.time.*;

class SubArrays 
{ 
    static void subArray(String s) 
    { 
        //Start time of the code
        Instant start = Instant.now();
        int n = s.length();
        for (int i=0; i <n; i++) 
        { 
            // Pick ending point of the current subarray 
            for (int j=i; j<n; j++) 
            { 
                // Print subarray between current starting and ending points 
                for (int k=i; k<=j; k++) {
                    System.out.print(s.charAt(k)+" "); 
              }
              System.out.println();
            } 
        }
        //End time of the code, to calculate elapsed time
         Instant end = Instant.now();
         Duration timeElapsed = Duration.between(start, end);
         System.out.println("Time taken: "+ timeElapsed.toMillis() +" milliseconds"); 
    } 
      
 
    public static void main(String[] args)  
    { 
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        System.out.println("All Non-empty Subarrays are:"); 
        subArray(s); 
          
    } 
} 