
# Time took : 8 mins


'''
Approach: continue untill head is not none or head.next is not none (these conditions bez the inner if statment)
check if the node.val is == nextnode.val, if it's equal then change the links and move to the next node
if not equal then move on untill you see node as None

Time Complexity: O(n) ; n = Total number of nodes in the linked list

'''

class Solution:
    def removeduplicates(self,head):
        if head == None:
            return head
        temphead = head
        while(head != None and head.next != None):
            if(head.val == head.next.val):
                head.next = head.next.next
            else:
                head = head.next
        return temphead
