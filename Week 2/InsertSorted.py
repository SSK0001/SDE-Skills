

class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class Solution:
    def __init__(self,node):
        self.head = node

    def insertsorted(self,insert_node):
        # Checking if the head is null - If its null insert the new node in that place
        if self.head == None:
            self.head = insert_node
            return self.head

        # Checking if the node belongs to any place in the middle
        tempnode = self.head
        prev = None
        while(tempnode != None):
            if tempnode.val > insert_node.val:
                tempnode.next = prev.next
                prev.next = tempnode
                return self.head
            prev = tempnode
            tempnode = tempnode.next

        # if both options fail we insert it at the end
        prev.next = insert_node
        return self.head
