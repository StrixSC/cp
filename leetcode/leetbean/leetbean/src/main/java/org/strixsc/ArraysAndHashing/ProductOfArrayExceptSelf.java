package org.strixsc.ArraysAndHashing;

import java.util.Arrays;
import java.util.stream.Collectors;

public class ProductOfArrayExceptSelf {
    static class Solution {
        static public int[] productExceptSelf(int[] nums) {
            int[] result = new int[nums.length];
            int prefixProduct = 1;
            for (int i = 0; i < nums.length; i++) {
                result[i] = prefixProduct;
                prefixProduct *= nums[i];
            }

            int suffixProduct = 1;
            for (int i = nums.length - 1; i >= 0; i--) {
                result[i] *= suffixProduct;
                suffixProduct *= nums[i];
            }
            return result;
        }
    }

    public static void main(String[] args) {
            System.out.println(
                    Arrays.stream(Solution.productExceptSelf(new int[]{1, 2, 3, 4})).mapToObj(String::valueOf).reduce((value, result) -> value + "," + result).stream().collect(Collectors.toList())
            );
    }
}
