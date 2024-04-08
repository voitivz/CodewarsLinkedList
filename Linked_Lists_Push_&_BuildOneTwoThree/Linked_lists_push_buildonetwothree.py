from preloaded import Node
    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
    

def build_one_two_three():
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head