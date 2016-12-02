class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,n,x):

        if n != None:
            x.next = n.next
            n.next = x
            x.prev = n
            if x.next != None:
                x.next.prev=x

        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None

        elif self.tail == n:
            self.tail = x

    def remove_node(self, n):           # deleting node function || bits added

        if n.prev != None:
            n.prev.next = n.next        # set the next node as prev node next node

        else:
            self.head = n.next          # set the linked list head node next

        if n.next != None:
            n.next.prev = n.prev        # set the prev node as next node prev

        else:
            self.tail = n.prev          # set the linked list head to prev node


    def display(self):

        values = []
        n = self.head
        while n != None:

            values.append(str(n.value))
            n = n.next

        print ("List: " , ", ".join(values))

if __name__ == '__main__':

    l = List()

    node_4 = Node(4)            # set variable to the Node()
    node_6 = Node(6)
    node_8 = Node(8)
    node_3 = Node(3)
    node_2 = Node(2)

    l.insert(None,node_4)
    l.insert(l.head,node_6)    # inserting a node
    l.insert(l.head,node_8)
    l.insert(l.tail,node_3)
    l.insert(l.tail,node_2)
    l.display()

    l.remove_node(node_4)     # remove specific node
    l.remove_node(node_2)
    l.display()

    l.remove_node(l.tail)     # delete node in tail loc
    l.display()
