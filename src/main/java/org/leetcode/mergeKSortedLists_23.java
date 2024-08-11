package org.leetcode;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class mergeKSortedLists_23 {

//     Definition for singly-linked list.
     public class ListNode {
         int val;
         ListNode next;
         ListNode() {}
         ListNode(int val) { this.val = val; }
         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }

    class Solution {
        public ListNode mergeKLists(ListNode[] lists) {
            if (lists.length == 0)
                return null;

            while(lists.length > 1){
                ArrayList<ListNode> mergedList = new ArrayList<>();
                for(int i = 0; i + 1 < lists.length; i += 2){
                    ListNode l1 = lists[i];
                    ListNode l2 = lists[i+1];
                    mergedList.add(mergeLists(l1, l2));
                }
                if(lists.length % 2 == 1)
                    mergedList.add(lists[lists.length - 1]);
                lists = mergedList.toArray(new ListNode[0]);
            }

            return lists[0];
        }

        public ListNode mergeLists(ListNode l1, ListNode l2){
            ListNode merged = new ListNode();
            ListNode curr = merged;
            while(l1 != null && l2 != null){
                if(l1.val < l2.val){
                    curr.next = l1;
                    l1 = l1.next;
                }
                else{
                    curr.next = l2;
                    l2 = l2.next;
                }
                curr = curr.next;
            }
            while(l1 != null){
                curr.next = l1;
                l1 = l1.next;
                curr = curr.next;
            }
            while(l2 != null){
                curr.next = l2;
                l2 = l2.next;
                curr = curr.next;
            }
            return merged.next;
        }


        public ListNode mergeKLists2(ListNode[] lists) {
            Map<Integer, Integer> map = new HashMap<>();
            for(int i = -10000; i <= 10000; i++){
                map.put(i, 0);
            }
            for(ListNode node: lists){
                ListNode curr = node;
                while(curr != null){
                    map.put(curr.val, map.get(curr.val)+1);
                    curr = curr.next;
                }
            }
            ListNode res = null;
            ListNode curr = null;
            for(int i = -10000; i <= 10000; i++){
                for(int j = 0; j < map.get(i); j++){
                    if (res == null) {
                        res = new ListNode(i);
                        curr = res;
                    } else {
                        curr.next = new ListNode(i);
                        curr = curr.next;
                    }
                }
            }
            return res;
        }
    }
}
