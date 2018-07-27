

import queue

def ReverseStack(stack):
    '''
    Reversing the stack
    '''
    if stack.empty():
        return stack

    q = queue.Queue()

    while(not stack.empty()):
        stackTop = stack.get()
        if q.empty() == True:
            q.put(stackTop)
        else:
            qLen = q.qsize()
            q.put(stackTop)
            while(qLen > 0):
                q.put(q.get())
                qLen -= 1

    while(not q.empty()):
        stack.put(q.get())

    return stack
