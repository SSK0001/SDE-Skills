# Time taken: 16 mins

'''
Approach: three conditions for this problem
1. new node has to be placed at the head: if statment
2. if new nodes to be placed in middle: while loop
3. new node to be placed at the end of the list: if neither of top 2, insert at end
'''

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
