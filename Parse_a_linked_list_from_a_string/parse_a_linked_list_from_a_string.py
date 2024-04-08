def linked_list_from_string(s):
    if s.lower() == 'null' or s.lower() == 'none':
        return None
    
    values = s.split(' -> ')
    head = Node(int(values[0]))
    current = head
    
    for value in values[1:]:
        if value.lower() == 'null' or value.lower() == 'none':
            current.next = None
        else:
            current.next = Node(int(value))
        current = current.next
    
    return head
