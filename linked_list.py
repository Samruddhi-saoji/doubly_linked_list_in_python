class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        #self.index = None #position in the linkedlist #starts at 0

# doubly linked list
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # length of the linked list


    #check if list is empty
    def is_empty(self):
        if self.head==None: #and self.tail==None:
            return True
        return False
    
    #insert and return node
    def insert_at_start(self, data):
        #new node to be inserted
        node = Node(data)

        #insert node
        if self.head is None:
            #list is empty
            self.head = node
            self.tail = node
        else: #list is not empty
            self.head.prev = node
            node.next = self.head
            
            #update head pointer
            self.head = node

        #update size value
        self.size += 1

        return node
    
    
    #insert node with given data value at given index 'i'
    def insert_at(self, i, data):
        #if index is invalid
        if i < 0 or i > self.size:
            print("Invalid index.")
            return None
        
        #if inserting at start 
        if i == 0:
            return self.insert_at_start(data)
        
        #inserting at the end
        elif i == self.size:
            return self.append(data)
        
        #inserting in the middle
        else : 
            #create the new node to be inserted
            temp = Node(data)

            #get the nodes at index i-1 and i
            node1 = self.get_node_at(i-1) #i-1
            node2 = node1.next #i

            #insert new node btw node1 and node2
            node1.next = temp
            temp.prev = node1
            node2.prev = temp
            temp.next = node2

            return temp


    def append(self, data):
        #new node to be inserted
        node = Node(data)

        #insert node
        if self.head is None:
            #list is empty
            self.head = node
            self.tail = node
        else: #list is not empty
            self.tail.next = node
            node.prev = self.tail
            
            #update tail pointer
            self.tail = node

        #update size value
        self.size += 1

        return node
    
        
    ###### delete #######
    #delete node with the given data value 
       #(if data occurrs multiple times in the list, then delete any node with that data value)
    def delete(self, data) :
        #if list is empty, return false
        if self.head is None:
            return False
        
        #get the node
        node = self.get_node(data)

        #delet the node
        return self.delete_node(node)


    #delete a given node
    def delete_node(self, node):
        #if list is empty or this node doesnt exist
        if node is None or self.head is None :
            return False

        #if it is head or tail node
        if node == self.head:
            return self.delete_head()
        elif node == self.tail:
            return self.delete_tail()
        else : #middle node 
            #get its neighbours
            node1 = node.prev
            node2 = node.next

            #update pointers
            node1.next = node2
            node2.prev = node1

            #update size
            self.size = self.size -1

            return True
    

    # delete node at the given index
    def delete_node_at(self, i):
        #get the node to be deleted
        node = self.get_node_at(i)

        #delete the node
        return self.delete_node(node)
    
    # delete node at start
    def delete_head(self):
        self.head = self.head.next
        self.head.prev = None

        self.size = self.size -1

        return True
    
    # delete node at end
    def delete_tail(self):
        self.tail = self.tail.prev
        self.tail.next = None

        self.size = self.size -1

        return True


    # find and return the node with data = x
        # return None if it doesnt exist
        # if x occurs multiple time, then return any node with that data value
    def get_node(self, x):
        #if its head or  tail node
        if self.head.data == x:
            return self.head
        if self.tail.data == x:
            return self.tail

        current = self.head.next
        #travrese the linked list
        while current.next:
            if current.data == x:
                return current
            current = current.next

        return None


    #get the node at the given index
    def get_node_at(self, i):
        if i<0 or i>=self.size:
            #index out of range
            return None
        
        current = self.head #node fro traversal
        for _ in range(i):
            current = current.next
        return current


    #print the linked list
    def display(self):
        current = self.head
        while current.next:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data)



    ######### update nodes data value #####
    def update_node(self, node, data):
        if node:
            node.data = data


    def update_node_at(self, index, data):
        #get the node to be updated
        node = self.get_node_at(index)

        #update the node if it exists
        if node:
            node.data = data


    #get the index of the first occurence of x
        #index strarts from 0
        # return -1 if it doesnt exists
    def get_index(self, x):
        temp = self.head #node for traversal

        for i in range(self.size-1):
            if temp.data == x:
                return i
            
            temp = temp.next

        return -1
    

    #get index of node
    def get_index_of(self, node):
        #if its the tail node
        if node == self.tail:
            return self.size - 1
        
        #traverse
        temp = self.head #node for traversal
        for i in range(self.size-1):
            if temp == node:
                return i
            
            temp = temp.next

        return -1
    

    #number of occurences of x
    def get_frequency(self, x):
        count = 0
        current = self.head
        while current:
            if current.data == x:
                count +=1

        return count
    

    #insert node before and after other nodes
    #insert x before the given node
    def insert_before(self, x, node2):
        if node2 is None:
            return None
        if node2 is self.head:
            return self.insert_at_start(x)
        
        node1 = node2.prev
        node = Node(x)

        node1.next = node
        node2.prev = node

        node.prev = node1
        node.next = node2

        #update size
        self.size = self.size +1

        return Node
    

    #insert x after the given node
    def insert_after(self, x, node1):
        if node1 is None:
            return None
        if node1 is self.tail:
            return self.append(x)
        
        node2 = node1.next
        node = Node(x)

        node1.next = node
        node2.prev = node

        node.prev = node1
        node.next = node2

        #update size
        self.size = self.size +1

        return Node




        





