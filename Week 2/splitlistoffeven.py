# Time taken : 18mins

'''

'''

class Solution:

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        evenhead = head.next

        odd = head
        even = evenhead

        while(odd.next != None and even.next != None):
            # temp = even.next
            odd.next = even.next
            even.next = odd.next.next
            odd = odd.next
            even = even.next

        odd.next = evenhead

        return head
