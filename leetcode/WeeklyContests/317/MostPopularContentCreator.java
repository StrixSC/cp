import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public List<List<String>> mostPopularCreator(String[] creators, String[] ids, int[] views) {
        
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int n = creators.length;
        for(int i = 0; i < n; i++) {
            int oldViews = map.get(creators[i]) | 0;
            String name = creators[i] + i;
            map.put(name, oldViews);
        }

        String highestKey = "";
        int highest = 0;
        for (String key : map.keySet()) {
            if(highest > map.get(key)) {
                highest = map.get(key);
                highestKey = key;
            }
        }

        String id = highestKey.substring(highestKey.length() - 1, highestKey.length());
        Integer id_int = new Integer(id);
        List<List<String>> res = Arrays.asList(Arrays.asList(creators[id_int], ids[id_int]));
        return res;
    }
}