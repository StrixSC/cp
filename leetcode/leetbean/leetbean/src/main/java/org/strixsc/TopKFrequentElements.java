package org.strixsc;

import java.util.*;
import java.util.stream.Collectors;

public class TopKFrequentElements {

    public static class Solution {
        public static int[] topKFrequentWithSort(int[] nums, int k) {
            Map<Integer, Integer> hm = new HashMap<>();

            // First establish how many occurrences:
            for (int i : nums)
            {
                if (hm.containsKey(i)) {
                    hm.put(i, hm.get(i) + 1);
                } else {
                    hm.put(i, 1);
                }
            }

            List<Map.Entry<Integer, Integer>> values = hm.entrySet().stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
                .collect(Collectors.toList());

            int[] toReturn = new int[k];
            for (int i = 0; i < k; i++) {
                toReturn[i] = values.get(i).getKey();
            }

            return toReturn;
        }

        public static int[] topKFrequentPQ(int[] nums, int k) {

            Map<Integer, Integer> hm = new HashMap<>();

            // First establish how many occurrences:
            for (int n : nums)
            {
                hm.put(n, hm.getOrDefault(n, 0) + 1);
            }

            Queue<Integer> q = new PriorityQueue<>((a, b) -> hm.get(b) - hm.get(a));

            for (Integer key : hm.keySet())
            {
                q.add(key);
            }

            int[] toReturn = new int[k];
            for (int i = 0; i < k; i++)
            {
                toReturn[i] = q.poll();
            }

            return toReturn;
        }

        public static int[] topKFrequent(int[] nums, int k) {
            // Buckets solution

            Map<Integer, Integer> hm = new HashMap<>();
            List<Integer> buckets[] = new ArrayList[nums.length + 1];

            // First establish how many occurrences:
            for (int n : nums)
            {
                hm.put(n, hm.getOrDefault(n, 0) + 1);
            }

            // Fill the buckets with their respective amounts of entries.
            for (Map.Entry<Integer, Integer> entry : hm.entrySet())
            {
                if(buckets[entry.getValue()] == null){
                    buckets[entry.getValue()] = new ArrayList<>();
                }
                buckets[entry.getValue()].add(entry.getKey());
            }

            // Traverse the buckets in reverse order and get the K elements with the most occurrences:
            List<Integer> toReturn = new ArrayList<>();
            for (int i = buckets.length - 1; i >= 0; i--)
            {
                if (buckets[i] != null)
                {
                    toReturn.addAll(buckets[i]);
                }
            }

            return toReturn.subList(0, k).stream().mapToInt(Integer::intValue).toArray();
        }
    }

    public static void main(String[] args) {
        System.out.println(Arrays.stream(Solution.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2)).mapToObj(String::valueOf).reduce((result, value) -> result + ", " + value).orElse(""));
    }
}
