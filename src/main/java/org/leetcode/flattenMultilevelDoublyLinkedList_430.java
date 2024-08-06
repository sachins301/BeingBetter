package org.leetcode;

class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};

public class flattenMultilevelDoublyLinkedList_430 {
    public Node flatten(Node head) {
        Node tail = flattenRecursion(head);
        return head;
    }

    public Node flattenRecursion(Node head){
        Node curr = head;
        while(curr != null){
            if(curr.child != null){
                Node childTail = flattenRecursion(curr.child);
                if(curr.next != null){
                    curr.next.prev = childTail;
                }
                childTail.next = curr.next;
                curr.next = curr.child;
                curr.child.prev = curr;
                curr.child = null;
            }
            if(curr.next != null)
                curr = curr.next;
            else
                break;
        }
        return curr;
    }
}
