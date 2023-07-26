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
    
    def insert_at_end(self, data): 
        # exception if llist is empty
        if self.head is None: 
            self.head = Node(data, None)
            return
        # else
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def remove_at(self, index): 
        # scenario 1: index isn't valid
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        # scenario 2: index = 0, i.e. remove head
        if index==0: 
            self.head = self.head.next
            return
        # scenario 3: 
        count = 0
        itr = self.head 
        while itr: 
            if count == index-1: 
                itr.next = itr.next.next 
                break
            itr = itr.next
            count += 1

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

    def insert_values(self, data_list): 
        self.head=None #??
        for i in data_list: 
            self.insert_at_end(i)

    def get_length(self): 
        count = 0 
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def insert_at(self, index, data): 
        # sc 1: invalid index
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        
        #sc 2: insert at index 0 
        if index==0: 
            self.insert_at_beginning(data)

        # sc 3: other indices
        count = 0
        itr = self.head
        while itr:
            if count == index-1: 
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(9)
    ll.insert_at_end(42)
    ll.insert_values([1, 2, 3])
    ll.print()
    ll.remove_at(0)
    ll.insert_at(1, "lol")
    ll.print()    
    