# Stack implementation

class Stack:

    def __init__(self,size):
        """
        initialize data structure.
        """
        self.stack = []
        self.size = size

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack)+1 > self.size:
            raise Exception('Stack Full')
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            raise Exception('Stack is empty, cannot pop')
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
