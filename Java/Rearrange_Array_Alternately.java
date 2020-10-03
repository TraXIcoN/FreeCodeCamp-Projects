import java.util.*;
public class Rearrange_Array_Alternately {
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
	    int t = in.nextInt();
        while(t>0){
        	int n = in.nextInt();
            int a[] = new int[n];
            for(int i=0;i<n;i++)
                a[i] = in.nextInt();
            int res[] = new int[n];
            int i = 0;
            int minI = 0, maxI = n-1;
            while(minI <= maxI){
                if(i%2==0){
                    res[i] = a[maxI--];
                }
                else{
                    res[i] = a[minI++];
                }
                i++;
            }
            for(int ele: res){
                System.out.print(ele + " ");
            }
            System.out.println();
            t--;
        }
        in.close();
    }
    
}
