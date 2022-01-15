import java.util.Arrays;
import java.util.Scanner;

public class test1
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        String[] strnk = scanner.nextLine().split(" ");
        int n = Integer.parseInt(strnk[0]);
        int k = Integer.parseInt(strnk[1]);

        String[] strL = scanner.nextLine().split(" ");
        int[] l = new int[n];
        double sum = 0;
        for (int i = 0; i < n; i++) {
            l[i] = Integer.parseInt(strL[i]);
            sum += l[i];
        }

        if (k == 0)
            System.out.println(Arrays.stream(l).max().getAsInt());
        else
        {
            double ideal = sum / (n + k);
            int q;
            if (ideal % 1 > 0)
                q = (int)ideal + 1;
            else
                q = (int)ideal;

            while (true)
            {
                int curCut = 0;
                for (double ll:l)
                {
                    if (ll/q > 1) {
                        if (ll % q > 0)
                            curCut += (int)ll/q;
                        else
                            curCut += (int)(ll/q - 1);
                    }
                }
                if (curCut > k) {
                    q += 1;
                    continue;
                }
                else
                {
                    System.out.println(q);
                    break;
                }
            }
        }
    }
}
