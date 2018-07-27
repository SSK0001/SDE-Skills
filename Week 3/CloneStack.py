# Clone Stack


def cloneStack(original):
    '''
    type original: original stack
    type clone: clone stack with this
    rtype: clone
    '''
    if len(original) == 0:
        return original

    tempStack = queue.LifoQueue()

    clone = []

    while(len(original) > 0):
        tempStack.put(original.pop())

    while(not tempStack.empty()):
        stackTop = tempStack.pop()
        original.append(stackTop)
        clone.append(stackTop)

    return clone
