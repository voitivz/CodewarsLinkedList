class Node:
    '''Node'''
    def __init__(self, data=None):
        '''init'''
        self.data = data
        self.next = None
    
class Context:
    '''Context'''
    def __init__(self, first, second):
        '''init'''
        self.first = first
        self.second = second
    
def alternating_split(head):
    '''alternating_split'''
    assert head and head.next
    a, b = Node(head.data), Node(head.next.data)
    result, head = Context(a, b), head.next.next
    while head:
        a.next = Node(head.data)
        a, b, head = b, a.next, head.next
    return result