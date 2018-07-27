# Clone Stack


def cloneStack(self,original):
    '''
    type original: original stack
    type clone: clone stack with this
    rtype: clone
    '''
    original = original.stack
    if len(original) == 0:
        return original
    tempStack = []
    clone = []
    while(len(original) > 0):
        tempStack.append(original.pop())
    while(len(tempStack) > 0):
        value = tempStack.pop()
        original.append(value)
        clone.append(value)
    return clone
