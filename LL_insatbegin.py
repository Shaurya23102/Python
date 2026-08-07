newnode = node(3)

def insatbegin(head, newnode):
    newnode.next = head   # point new node to old head
    head = newnode         # update head
    return head           # return new head
head = insatbegin(head,newnode)
printll(head)
