package org.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class GroupAnagrams_49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(String s: strs){
            char[] sArray = s.toCharArray();
            Arrays.sort(sArray);
            String key = new String(sArray);
            if(map.containsKey(key)){
                map.get(key).add(s);
            } else{
                map.put(key, new ArrayList<>(Arrays.asList(s)));
            }
        }
        return new ArrayList<>(map.values());
    }
}
