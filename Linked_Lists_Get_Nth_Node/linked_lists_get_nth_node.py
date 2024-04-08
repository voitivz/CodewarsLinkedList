from preloaded import Node

def get_nth(node, index):
    if not isinstance(index,int):
        raise TypeError
    if index < 0:
        raise TypeError
    if node == None:
        raise TypeError
    cur = node
    for i in range(index):
        if cur.next == None and i != index:
            raise IndexError
        cur = cur.next
    return cur