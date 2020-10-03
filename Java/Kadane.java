import java.io.*;
class Kadane {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt( in .readLine());
        while (t > 0) {
            int n = Integer.parseInt( in .readLine());
            String line = in .readLine();
            String[] strs = line.trim().split("\\s+");
            int a[] = new int[n];
            int sum = 0, max = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(strs[i]);
                sum = Math.max(a[i], sum + a[i]);
                max = Math.max(max, sum);
            }
            System.out.println(max);
            t--;
        }
    }
}