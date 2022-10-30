package leetcode.tmp;

import java.util.ArrayList;

public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // We need to partition each array.
        double res = 0.0;
        boolean isOdd = ((nums1.length + nums2.length) % 2 == 0);

        int left = nums1.length/2;
        int right = nums2.length/2;

        if(!isOdd) {
            while(left <= right) {
                
            }
        }
        return res;
    }

    public static void main(String args[]) {
        MedianOfTwoSortedArrays sol = new MedianOfTwoSortedArrays();
        int first[] = {1,2};
        int second[] = {3, 4};
        double res = sol.findMedianSortedArrays(first, second);
        System.out.println(res);
    }
}
