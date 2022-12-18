package leetcode.tmp;

public class MaxProfit {
    public int maxProfit(int[] prices) {
        int min_index = 0;
        int min = 0;
        int max = 0;
        for (int i = 0; i != prices.length; i++) {
            if (min > prices[i]) {
                min = prices[i];
                min_index = i;
            }
        }

        for (int i = min_index + 1; i != prices.length; i++) {
            max = max > prices[i] ? max : prices[i];
        }

        return Math.abs(max - min);
    }
}
