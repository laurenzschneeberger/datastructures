## implementing a linked list in python

class Node: 
    def __init__(self, data=None, next=None):
        # a node consists of a datapoint...
        self.data = data
        # ...and a pointer to the next node
        self.next = next

class LinkedList: 
    def __init__(self):
        # a linked list consists of nodes, which we defined above. 
        # it also needs a head: 
        self.head = None

    def insert_at_beginning(self, data):
        #creates a node object with some data and a head=None
        node = Node(data, self.head) 
        #sets the list's head to point to the current node
        self.head = node 

    def print(self):
        if self.head is None: #if the head doesn't tell us where to go, our list is empty
            print("Linked list is empty")
            return
        itr = self.head
        #a string used to print a graphical representation of the l-list
        llstr = '' 
        #the while loop will only run while itr is true, i.e. it contains a value. So if it is None, this code won't execute
        while itr: 
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(9)
    ll.print()
    