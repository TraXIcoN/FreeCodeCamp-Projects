import java.io.*;
class Kth_SmallestElement {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt( in .readLine());
        while (t > 0) {
            int n = Integer.parseInt( in .readLine());
            PriorityQueue < Integer > pq = new PriorityQueue < Integer > (Collections.reverseOrder());
            String s[] = in .readLine().trim().split(" ");
            int k = Integer.parseInt( in .readLine());
            for (int i = 0; i < n; i++)
                pq.add(Integer.parseInt(s[i]));
            for (int i = 0; i < n - k; i++)
                pq.remove();
            System.out.println(pq.peek());
            t--;
        }
    }
}