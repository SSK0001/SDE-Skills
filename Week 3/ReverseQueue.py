
# Reverse the data in queue using stack
import queue
def reverseQueue(q):
    '''
    Python operations of queue
    import queue
    q = queue.Queue()
    q.put(10)
    q.get() => 10
    q.empty() => True
    q.maxsize => 0 (bez we havent set any)
    q.full() => False (bez we havent set any)

    q = queue.LifoQueue()
    q.put(10)
    q.put(20)
    q.get() => 20
    q.empty() => True
    q.maxsize => 0 (bez we havent set any)
    q.full() => False (bez we havent set any)
    '''

    if q.empty():
        return queue

    stack = queue.LifoQueue()

    while(not q.empty()):
        stack.put(q.get())

    while(not stack.empty()):
        q.put(stack.get())

    return q


q1 = queue.Queue()
q1.put(10)
q1.put(20)
q1.put(30)

q2 = reverseQueue(q1)

while(not q2.empty()):
    print(q2.get())
