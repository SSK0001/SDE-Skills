
# Time took : 10 mins
'''
Approach 1: can create a additional linked list to store the entire list while traversing the list1 and list2 with two diffrent pointer
            Time complexity : O(n); Space Complexity: o(n) {Cloning the two diffrent lists}
Approach 2: Make a fake node up front and stich the node as you move along list1 and list2 with two diffrent pointers
            Time Complexity: O(n); Space complexity: O(fake node memory)
'''


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        temphead = ListNode(0)
        head = temphead

        while(list1 != None and list2 != None):
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        if list1 == None:
            head.next = list2
        elif list2 == None:
            head.next = list1

        return temphead.next
